from src.settings import DATABASE


TORTOISE_ORM = {
    "connections": 
     {"default": {
                "engine": "tortoise.backends.asyncpg",
                "credentials": {
                    "database": DATABASE.POSTGRESQL_DATABASE,
                    "host": DATABASE.POSTGRESQL_HOSTNAME_DOCKER,
                    "password": DATABASE.POSTGRESQL_PASSWORD,
                    "user": DATABASE.POSTGRESQL_USERNAME,
                    "port": 5432
                }
            },
    },
    "apps": {
        "models": {
            "models": [
                "aerich.models",
                "src.database.models", 
            ],
            "default_connection": "default"
        }
    }
}
