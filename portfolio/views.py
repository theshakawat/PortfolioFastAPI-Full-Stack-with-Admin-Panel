from fastapi import APIRouter, Request, Form
from core.config import templates, mail_configure
from fastapi_mail import FastMail, MessageSchema, MessageType
from pydantic import EmailStr
from core import variable

from portfolio.models import (
    Profile,
    Service,
    Skill,
    Education,
    Employment,
    Testimonial,
    Portfolio,
)
from portfolio.schemas import EmailSchema

router = APIRouter()


@router.get("/")
async def show_profile(request: Request):
    profile = await Profile.first()
    services = await Service.filter(is_active=True).order_by("serial")
    skills = await Skill.filter(is_active=True).order_by("serial")
    education = await Education.filter(is_active=True).order_by("-from_date")
    employment = await Employment.filter(is_active=True).order_by("-from_date")
    testimonials = await Testimonial.filter(is_active=True).order_by("serial")
    portfolio = await Portfolio.filter(is_active=True).order_by("-serial")
    # portfolio_types = await Portfolio.filter(is_active=True).order_by("-serial").values_list("type", flat=True)
    # portfolio_unique_types = list(set(portfolio_types))

    # ✅ Fallback Profile if None
    if not profile:
        profile = {"name": "Guest User", "bio": "Welcome!", "email": "guest@example.com"}

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "profile": profile,
            "services": services,
            "skills": skills,
            "education": education,
            "employment": employment,
            "testimonials": testimonials,
            "portfolio": portfolio,
            "portfolio_unique_types": variable.list_of_project_type_short,
        },
    )


mailSending = FastMail(mail_configure)


@router.post("/send-email")
async def send_email(
        name: str = Form(...),
        email: EmailStr = Form(...),
        subject: str = Form(...),
        message: str = Form(...)
):
    email_data = EmailSchema(name=name, email=email, subject=subject, message=message)
    msg = MessageSchema(
        subject=f"{email_data.subject}",
        recipients=["md.shakawat.hossain@yandex.com"],
        body=f"Name:\n{email_data.name}\n\nEmail:\n{email_data.email}\n\nMessage:\n{email_data.message}",
        subtype=MessageType.plain,
        reply_to=[email_data.email]
    )
    await mailSending.send_message(msg)
    return {"success": True, "message": "Email sent successfully!"}
