from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType

DATABASE_URL = "sqlite://db.sqlite3"

# Define static files configuration
static_files = StaticFiles(directory="static")

#template configure
templates = Jinja2Templates(directory="templates")

#contact mail configure
mail_configure = ConnectionConfig(
    MAIL_USERNAME="",
    MAIL_PASSWORD="",
    MAIL_FROM="",
    MAIL_PORT=465,
    MAIL_SERVER="",
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True
)