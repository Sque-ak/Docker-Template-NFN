from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise

from src.database.register import register_tortoise 
from src.database.config import TORTOISE_ORM 
from src.settings import DATABASE, SETTINGS

# enable schemas to read relationship between models
Tortoise.init_models(["src.database.models"], "models")

from src.routes import users

app = FastAPI(
    title=f'{SETTINGS.APP_NAME} {SETTINGS.APP_VERSION}',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)

@app.get("/")
def home():
    return DATABASE.POSTGRESQL_HOSTNAME
