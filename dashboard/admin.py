from datetime import date

from fastapi import APIRouter, Depends, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse

from core.config import templates
from portfolio.models import Service, Skill, Education, Employment, Testimonial, Portfolio, Profile
from typing import Optional
from core import variable

admin_router = APIRouter()


# Authentication
async def get_current_user(request: Request):
    user = request.session.get("user")
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return user


# Common Admin Routes
@admin_router.get("/admin", response_class=HTMLResponse)
async def admin_dashboard(request: Request, user: str = Depends(get_current_user)):
    return templates.TemplateResponse("dashboard/dashboard.html", {
        "request": request,
        "skills_count": await Skill.filter(is_active=True).count(),
        "services_count": await Service.filter(is_active=True).count(),
        "portfolios_count": await Portfolio.all().count(),
        "recent_services": await Service.all().order_by("-id").limit(5),
        "recent_testimonials": await Testimonial.all().order_by("-id").limit(5),
        "recent_educations": await Education.all().order_by("-id").limit(5),
        "recent_employments": await Employment.all().order_by("-id").limit(5)
    })


@admin_router.get("/admin/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("dashboard/login.html", {"request": request})


@admin_router.post("/admin/login")
async def perform_login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "admin":
        request.session["user"] = username
        return RedirectResponse(url="/admin", status_code=303)
    return RedirectResponse(url="/admin/login?error=invalid_credentials", status_code=303)


@admin_router.get("/admin/logout")
async def logout(request: Request):
    request.session.pop("user", None)
    return RedirectResponse(url="/admin/login", status_code=303)


# Service CRUD (You already have this, keeping for completeness)
@admin_router.get("/admin/services", response_class=HTMLResponse)
async def list_services(request: Request, user: str = Depends(get_current_user)):
    services = await Service.all().order_by("serial")
    return templates.TemplateResponse("dashboard/service/list.html", {
        "request": request,
        "services": services
    })


# Skill CRUD
@admin_router.get("/admin/skills", response_class=HTMLResponse)
async def list_skills(request: Request, user: str = Depends(get_current_user)):
    skills = await Skill.all().order_by("serial")
    return templates.TemplateResponse("dashboard/skill/list.html", {
        "request": request,
        "skills": skills
    })


@admin_router.get("/admin/skills/create", response_class=HTMLResponse)
async def create_skill_form(request: Request, user: str = Depends(get_current_user)):
    return templates.TemplateResponse("dashboard/skill/create.html", {"request": request})


@admin_router.post("/admin/skills/create")
async def create_skill(
        request: Request,
        title: str = Form(...),
        percent: int = Form(...),
        serial: int = Form(0),
        is_active: bool = Form(False),
        user: str = Depends(get_current_user)
):
    await Skill.create(
        title=title,
        percent=percent,
        serial=serial,
        is_active=is_active
    )
    return RedirectResponse(url="/admin/skills", status_code=303)


# Education CRUD
@admin_router.get("/admin/educations", response_class=HTMLResponse)
async def list_educations(request: Request, user: str = Depends(get_current_user)):
    educations = await Education.all().order_by("-from_date")
    return templates.TemplateResponse("dashboard/education/list.html", {
        "request": request,
        "educations": educations
    })


@admin_router.get("/admin/educations/create", response_class=HTMLResponse)
async def create_education_form(request: Request, user: str = Depends(get_current_user)):
    return templates.TemplateResponse("dashboard/education/create.html", {"request": request})


@admin_router.post("/admin/educations/create")
async def create_education(
        request: Request,
        degree: str = Form(...),
        from_date: date = Form(...),
        to_date: date = Form(None),
        organization_name: str = Form(...),
        location: str = Form(...),
        website: str = Form(None),
        description: str = Form(None),
        is_active: bool = Form(False),
        is_present: bool = Form(False),
        user: str = Depends(get_current_user)
):
    education = await Education.create(
        degree=degree,
        from_date=from_date,
        to_date=to_date,
        organization_name=organization_name,
        location=location,
        website=website,
        description=description,
        is_active=is_active,
        is_present=is_present
    )
    return RedirectResponse(url="/admin/educations", status_code=303)


@admin_router.get("/admin/educations/edit/{id}", response_class=HTMLResponse)
async def edit_education_form(request: Request, id: int, user: str = Depends(get_current_user)):
    education = await Education.get_or_none(id=id)
    if not education:
        raise HTTPException(status_code=404, detail="Education not found")
    return templates.TemplateResponse("dashboard/education/edit.html", {
        "request": request,
        "education": education
    })


@admin_router.post("/admin/educations/edit/{id}")
async def update_education(
        request: Request,
        id: int,
        degree: str = Form(...),
        from_date: date = Form(...),
        to_date: date = Form(None),
        organization_name: str = Form(...),
        location: str = Form(...),
        website: str = Form(None),
        description: str = Form(None),
        is_active: bool = Form(False),
        is_present: bool = Form(False),
        user: str = Depends(get_current_user)
):
    education = await Education.get_or_none(id=id)
    if not education:
        raise HTTPException(status_code=404, detail="Education not found")

    education.degree = degree
    education.from_date = from_date
    education.to_date = to_date
    education.organization_name = organization_name
    education.location = location
    education.website = website
    education.description = description
    education.is_active = is_active
    education.is_present = is_present
    await education.save()

    return RedirectResponse(url="/admin/educations", status_code=303)


@admin_router.post("/admin/educations/delete/{id}")
async def delete_education(request: Request, id: int, user: str = Depends(get_current_user)):
    education = await Education.get_or_none(id=id)
    if education:
        await education.delete()
    return RedirectResponse(url="/admin/educations", status_code=303)


# Employment CRUD
@admin_router.get("/admin/employments", response_class=HTMLResponse)
async def list_employments(request: Request, user: str = Depends(get_current_user)):
    employments = await Employment.all().order_by("-from_date")
    return templates.TemplateResponse("dashboard/employment/list.html", {
        "request": request,
        "employments": employments
    })


@admin_router.get("/admin/employments/create", response_class=HTMLResponse)
async def create_employment_form(request: Request, user: str = Depends(get_current_user)):
    return templates.TemplateResponse("dashboard/employment/create.html", {"request": request})


@admin_router.post("/admin/employments/create")
async def create_employment(
        request: Request,
        position: str = Form(...),
        from_date: date = Form(...),
        to_date: date = Form(None),
        organization_name: str = Form(...),
        location: str = Form(None),
        website: str = Form(None),
        responsibilities: str = Form(...),
        achievement: str = Form(None),
        is_active: bool = Form(False),
        is_present: bool = Form(False),
        user: str = Depends(get_current_user)
):
    await Employment.create(
        position=position,
        from_date=from_date,
        to_date=to_date,
        organization_name=organization_name,
        location=location,
        website=website,
        responsibilities=responsibilities,
        achievement=achievement,
        is_active=is_active,
        is_present=is_present
    )
    return RedirectResponse(url="/admin/employments", status_code=303)


# Employment Edit/Delete
@admin_router.get("/admin/employments/edit/{id}", response_class=HTMLResponse)
async def edit_employment_form(request: Request, id: int, user: str = Depends(get_current_user)):
    employment = await Employment.get_or_none(id=id)
    if not employment:
        raise HTTPException(status_code=404, detail="Employment not found")
    return templates.TemplateResponse("dashboard/employment/edit.html", {
        "request": request,
        "employment": employment
    })


@admin_router.post("/admin/employments/edit/{id}")
async def update_employment(
        request: Request,
        id: int,
        position: str = Form(...),
        from_date: date = Form(...),
        to_date: date = Form(None),
        organization_name: str = Form(...),
        location: str = Form(None),
        website: str = Form(None),
        responsibilities: str = Form(...),
        achievement: str = Form(None),
        is_active: bool = Form(False),
        is_present: bool = Form(False),
        user: str = Depends(get_current_user)
):
    employment = await Employment.get_or_none(id=id)
    if not employment:
        raise HTTPException(status_code=404, detail="Employment not found")

    employment.position = position
    employment.from_date = from_date
    employment.to_date = to_date
    employment.organization_name = organization_name
    employment.location = location
    employment.website = website
    employment.responsibilities = responsibilities
    employment.achievement = achievement
    employment.is_active = is_active
    employment.is_present = is_present
    await employment.save()

    return RedirectResponse(url="/admin/employments", status_code=303)


@admin_router.post("/admin/employments/delete/{id}")
async def delete_employment(request: Request, id: int, user: str = Depends(get_current_user)):
    employment = await Employment.get_or_none(id=id)
    if employment:
        await employment.delete()
    return RedirectResponse(url="/admin/employments", status_code=303)


# Testimonial CRUD
@admin_router.get("/admin/testimonials", response_class=HTMLResponse)
async def list_testimonials(request: Request, user: str = Depends(get_current_user)):
    testimonials = await Testimonial.all().order_by("serial")
    return templates.TemplateResponse("dashboard/testimonial/list.html", {
        "request": request,
        "testimonials": testimonials
    })


@admin_router.get("/admin/testimonials/create", response_class=HTMLResponse)
async def create_testimonial_form(request: Request, user: str = Depends(get_current_user)):
    return templates.TemplateResponse("dashboard/testimonial/create.html", {"request": request})


@admin_router.post("/admin/testimonials/create")
async def create_testimonial(
        request: Request,
        quote_owner: str = Form(...),
        role: str = Form(...),
        quote: str = Form(...),
        serial: int = Form(0),
        is_active: bool = Form(False),
        user: str = Depends(get_current_user)
):
    await Testimonial.create(
        quote_owner=quote_owner,
        role=role,
        quote=quote,
        serial=serial,
        is_active=is_active
    )
    return RedirectResponse(url="/admin/testimonials", status_code=303)


@admin_router.get("/admin/testimonials/edit/{id}", response_class=HTMLResponse)
async def edit_testimonial_form(request: Request, id: int, user: str = Depends(get_current_user)):
    testimonial = await Testimonial.get_or_none(id=id)
    if not testimonial:
        raise HTTPException(status_code=404, detail="Testimonial not found")
    return templates.TemplateResponse("dashboard/testimonial/edit.html", {
        "request": request,
        "testimonial": testimonial
    })


@admin_router.post("/admin/testimonials/edit/{id}")
async def update_testimonial(
        request: Request,
        id: int,
        quote_owner: str = Form(...),
        role: str = Form(...),
        quote: str = Form(...),
        serial: int = Form(0),
        is_active: bool = Form(False),
        user: str = Depends(get_current_user)
):
    testimonial = await Testimonial.get_or_none(id=id)
    if not testimonial:
        raise HTTPException(status_code=404, detail="Testimonial not found")

    testimonial.quote_owner = quote_owner
    testimonial.role = role
    testimonial.quote = quote
    testimonial.serial = serial
    testimonial.is_active = is_active
    await testimonial.save()

    return RedirectResponse(url="/admin/testimonials", status_code=303)


@admin_router.post("/admin/testimonials/delete/{id}")
async def delete_testimonial(request: Request, id: int, user: str = Depends(get_current_user)):
    testimonial = await Testimonial.get_or_none(id=id)
    if testimonial:
        await testimonial.delete()
    return RedirectResponse(url="/admin/testimonials", status_code=303)


# Portfolio CRUD
@admin_router.get("/admin/portfolios", response_class=HTMLResponse)
async def list_portfolios(request: Request, user: str = Depends(get_current_user)):
    portfolios = await Portfolio.all().order_by("-serial")
    return templates.TemplateResponse("dashboard/portfolio/list.html", {
        "request": request,
        "portfolios": portfolios
    })


@admin_router.get("/admin/portfolios/create", response_class=HTMLResponse)
async def create_portfolio_form(request: Request, user: str = Depends(get_current_user)):
    return templates.TemplateResponse("dashboard/portfolio/create.html", {"request": request})


@admin_router.post("/admin/portfolios/create")
async def create_portfolio(
        request: Request,
        type: str = Form(None),
        title: str = Form(...),
        description: str = Form(None),
        client: str = Form(None),
        image_url: str = Form(None),
        is_open_source: bool = Form(False),
        technology: str = Form(None),
        serial: int = Form(0),
        is_active: bool = Form(False),
        project_url: str = Form(None),
        user: str = Depends(get_current_user)
):
    await Portfolio.create(
        type=type,
        title=title,
        description=description,
        client=client,
        image_url=image_url,
        is_open_source=is_open_source,
        technology=technology,
        serial=serial,
        is_active=is_active,
        project_url=project_url
    )
    return RedirectResponse(url="/admin/portfolios", status_code=303)


# Portfolio Edit/Delete
@admin_router.get("/admin/portfolios/edit/{id}", response_class=HTMLResponse)
async def edit_portfolio_form(request: Request, id: int, user: str = Depends(get_current_user)):
    portfolio = await Portfolio.get_or_none(id=id)
    if not portfolio:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return templates.TemplateResponse("dashboard/portfolio/edit.html", {
        "request": request,
        "portfolio": portfolio,
        "portfolio_unique_types":variable.list_of_project_type
    })


@admin_router.post("/admin/portfolios/edit/{id}")
async def update_portfolio(
        request: Request,
        id: int,
        type: str = Form(None),
        title: str = Form(...),
        description: str = Form(None),
        client: str = Form(None),
        image_url: str = Form(None),
        is_open_source: bool = Form(False),
        technology: str = Form(None),
        serial: int = Form(0),
        is_active: bool = Form(False),
        project_url: str = Form(None),
        user: str = Depends(get_current_user)
):
    portfolio = await Portfolio.get_or_none(id=id)
    if not portfolio:
        raise HTTPException(status_code=404, detail="Portfolio not found")

    portfolio.type = type
    portfolio.title = title
    portfolio.description = description
    portfolio.client = client
    portfolio.image_url = image_url
    portfolio.is_open_source = is_open_source
    portfolio.technology = technology
    portfolio.serial = serial
    portfolio.is_active = is_active
    portfolio.project_url = project_url
    await portfolio.save()

    return RedirectResponse(url="/admin/portfolios", status_code=303)


@admin_router.post("/admin/portfolios/delete/{id}")
async def delete_portfolio(request: Request, id: int, user: str = Depends(get_current_user)):
    portfolio = await Portfolio.get_or_none(id=id)
    if portfolio:
        await portfolio.delete()
    return RedirectResponse(url="/admin/portfolios", status_code=303)


# Edit/Delete Routes for All Models (example for Service)
@admin_router.get("/admin/services/edit/{id}", response_class=HTMLResponse)
async def edit_service_form(request: Request, id: int, user: str = Depends(get_current_user)):
    service = await Service.get_or_none(id=id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return templates.TemplateResponse("dashboard/service/edit.html", {
        "request": request,
        "service": service
    })


@admin_router.post("/admin/services/edit/{id}")
async def update_service(
        request: Request,
        id: int,
        title: str = Form(...),
        description: str = Form(...),
        icon_id: str = Form(None),
        serial: int = Form(0),
        is_active: bool = Form(False),
        user: str = Depends(get_current_user)
):
    service = await Service.get_or_none(id=id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")

    service.title = title
    service.description = description
    service.icon_id = icon_id
    service.serial = serial
    service.is_active = is_active
    await service.save()

    return RedirectResponse(url="/admin/services", status_code=303)


@admin_router.post("/admin/services/delete/{id}")
async def delete_service(request: Request, id: int, user: str = Depends(get_current_user)):
    service = await Service.get_or_none(id=id)
    if service:
        await service.delete()
    return RedirectResponse(url="/admin/services", status_code=303)


# Skill Edit/Delete
@admin_router.get("/admin/skills/edit/{id}", response_class=HTMLResponse)
async def edit_skill_form(request: Request, id: int, user: str = Depends(get_current_user)):
    skill = await Skill.get_or_none(id=id)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    return templates.TemplateResponse("dashboard/skill/edit.html", {
        "request": request,
        "skill": skill
    })


@admin_router.post("/admin/skills/edit/{id}")
async def update_skill(
        request: Request,
        id: int,
        title: str = Form(...),
        percent: int = Form(...),
        serial: int = Form(0),
        is_active: bool = Form(False),
        user: str = Depends(get_current_user)
):
    skill = await Skill.get_or_none(id=id)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")

    skill.title = title
    skill.percent = percent
    skill.serial = serial
    skill.is_active = is_active
    await skill.save()

    return RedirectResponse(url="/admin/skills", status_code=303)


@admin_router.post("/admin/skills/delete/{id}")
async def delete_skill(request: Request, id: int, user: str = Depends(get_current_user)):
    skill = await Skill.get_or_none(id=id)
    if skill:
        await skill.delete()
    return RedirectResponse(url="/admin/skills", status_code=303)


# Profile CRUD
@admin_router.get("/admin/profile", response_class=HTMLResponse)
async def edit_profile(request: Request, user: str = Depends(get_current_user)):
    profile = await Profile.first()
    return templates.TemplateResponse("dashboard/profile/edit.html", {
        "request": request,
        "profile": profile
    })


@admin_router.post("/admin/profile/update")
async def update_profile(
        request: Request,
        name: str = Form(...),
        job_title: str = Form(...),
        bio_title: str = Form(...),
        bio: str = Form(...),
        email: Optional[str] = Form(None),
        phone: Optional[str] = Form(None),
        spoken_language: Optional[str] = Form(None),
        nationality: Optional[str] = Form(None),
        address: Optional[str] = Form(None),
        freelance: Optional[str] = Form(None),
        avatar_url: Optional[str] = Form(None),
        cv_url: Optional[str] = Form(None),
        user: str = Depends(get_current_user)
):
    profile = await Profile.first()
    if not profile:
        profile = await Profile.create()

    # Update all fields
    await profile.update_from_dict({
        'name': name,
        'job_title': job_title,
        'bio_title': bio_title,
        'bio': bio,
        'email': email,
        'phone': phone,
        'spoken_language': spoken_language,
        'nationality': nationality,
        'address': address,
        'freelance': freelance,
        'avatar_url': avatar_url,
        'cv_url': cv_url
    }).save()

    return RedirectResponse(url="/admin", status_code=303)


# Service Create Routes
@admin_router.get("/admin/services/create", response_class=HTMLResponse)
async def create_service_form(request: Request, user: str = Depends(get_current_user)):
    return templates.TemplateResponse(
        "dashboard/service/create.html",
        {"request": request}
    )


@admin_router.post("/admin/services/create")
async def create_service(
        request: Request,
        title: str = Form(...),
        description: str = Form(...),
        icon_id: str = Form(None),
        serial: int = Form(0),
        is_active: bool = Form(False),
        user: str = Depends(get_current_user)
):
    try:
        await Service.create(
            title=title,
            description=description,
            icon_id=icon_id,
            serial=serial,
            is_active=is_active
        )
        return RedirectResponse(url="/admin/services", status_code=303)
    except Exception as e:
        return templates.TemplateResponse(
            "dashboard/service/create.html",
            {
                "request": request,
                "error": f"Error creating service: {str(e)}"
            },
            status_code=400
        )
