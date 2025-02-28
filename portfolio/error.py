from starlette.exceptions import HTTPException as StarletteHTTPException
from core.config import templates
from fastapi import Request
from fastapi.responses import HTMLResponse


async def custom_404_handler(request: Request, exc: StarletteHTTPException):
    """Custom 404 error handler."""
    if exc.status_code == 404:
        return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
    return HTMLResponse(f"<h1>{exc.detail}</h1>", status_code=exc.status_code)
