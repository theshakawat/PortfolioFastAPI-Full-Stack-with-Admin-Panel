from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from core.config import DATABASE_URL
from portfolio.serializers import router as portfolio_serializers
from portfolio.views import router as portfolio_views
from core import config
from portfolio.error import custom_404_handler
from dashboard.admin import admin_router
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI(
    docs_url=None,  # Disable Swagger UI
    redoc_url=None,  # Disable ReDoc UI
    openapi_url=None  # Disable OpenAPI JSON
    # docs_url="/custom-docs",  # Change the Swagger docs and redoc URL here
)

# static files
app.mount('/static', config.static_files, name='static')

# route register
app.include_router(portfolio_serializers, prefix="/portfolio", tags=["Portfolio"])
app.include_router(portfolio_views, prefix="", tags=["Profile"])
app.include_router(admin_router)

# ✅ Register the error handler here
app.add_exception_handler(404, custom_404_handler)

# Tortoise ORM database initialization
register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": ["portfolio.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

app.add_middleware(
    SessionMiddleware,
    secret_key="secret_key",
    session_cookie="admin_session"
)

# For local running---
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

# For production run only---
# uvicorn main:app --host 0.0.0.0 --port $PORT
