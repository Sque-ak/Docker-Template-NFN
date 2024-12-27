from fastapi import HTTPException, status
from passlib.context import CryptContext
from tortoise.exceptions import DoesNotExist, IntegrityError

from src.database.models import Users
from src.schemas.users import UserOutSchema
from src.schemas.token import Status

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def create_user(user) -> UserOutSchema:
    user.password = pwd_context.encrypt(user.password)

    try:
        user_object = await Users.create(**user.dict(exclude_unset=True))
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Sorry, that username already exists.")
    
    return await UserOutSchema.from_tortoise_orm(user_object)

async def delete_user(user_id, current_user) -> Status:
    try:
        db_user = await UserOutSchema.from_queryset_single(Users.get(id=user_id))
    except DoesNotExist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {user_id} not found")
    
    if db_user.id == current_user.id:
        delete_count = await Users.filter(id=user_id).delete()
        if not delete_count:
            raise HTTPException(status_code=404, detail=f"User {user_id} not found")
        return Status(message=f"Deleted user {user_id}")
    
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to delete")
