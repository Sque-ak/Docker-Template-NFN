from datetime import datetime, timedelta, timezone
from typing import Optional, Any

from fastapi import Depends, HTTPException, Request, status
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.security import OAuth2
from fastapi.security.utils import get_authorization_scheme_param
from jose import JWTError, jwt
from tortoise.exceptions import DoesNotExist

from src.schemas.token import TokenData
from src.schemas.users import UserOutSchema
from src.database.models import Users
from src.settings import AUTH

class OAuth2PasswordBearerCookie(OAuth2):
    def __init__(self, token_url: str, scheme_name: str = None, scopes: dict = None, auto_error: bool = True):
        if not scopes:
            scopes = {}

        flows = OAuthFlowsModel(password={"tokenUrl": token_url, "scopes":scopes})
        super().__init__(flows=flows, scheme_name=scheme_name, auto_error=auto_error)

    async def __call__(self, request: Request) -> Optional[str]:
        authorization: str = request.cookies.get("Authorization")
        scheme, param = get_authorization_scheme_param(authorization)

        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None
            
        return param
    
security = OAuth2PasswordBearerCookie(token_url="/login")

def create_access_token(data:dict, expires_data: Optional[timedelta] = None):
    to_encode = data.copy()
    
    if expires_data:
        expire = datetime.now(timezone.utc) + expires_data
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    
    to_encode.update({"exp":expire})
    encode_jwt = jwt.encode(to_encode, AUTH.SECRET_KEY, algorithm=AUTH.ALGORITHM)

    return encode_jwt

async def get_current_user(token: str = Depends(security)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload: dict[str, Any]  = jwt.decode(token, AUTH.SECRET_KEY, algorithms=AUTH.ALGORITHM)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    try:
        user = await UserOutSchema.from_queryset_single(Users.get(username=token_data.username))
    except DoesNotExist:
        raise credentials_exception

    return user