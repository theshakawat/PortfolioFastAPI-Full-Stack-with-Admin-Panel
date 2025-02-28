from tortoise import Tortoise
from core.config import DATABASE_URL

async def init_db():
    await Tortoise.init(
        db_url=DATABASE_URL, modules={"models": ["portfolio.models"]}
    )
    await Tortoise.generate_schemas()
