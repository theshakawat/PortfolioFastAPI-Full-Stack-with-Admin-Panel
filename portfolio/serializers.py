from fastapi import APIRouter, HTTPException
from tortoise.exceptions import DoesNotExist
from typing import List
from portfolio.models import Profile, Service, Skill, Education, Employment, Testimonial, Portfolio
from portfolio.schemas import (
    ProfileCreate, ProfileUpdate, ProfileInResponse,
    ServiceCreate, ServiceUpdate, ServiceInResponse,
    SkillCreate, SkillUpdate, SkillInResponse,
    EducationCreate, EducationUpdate, EducationInResponse,
    EmploymentCreate, EmploymentUpdate, EmploymentInResponse,
    TestimonialCreate, TestimonialUpdate, TestimonialInResponse,
    PortfolioCreate, PortfolioUpdate, PortfolioInResponse
)

router = APIRouter()


# Profile Routes
@router.post("/profiles/", response_model=ProfileInResponse)
async def create_profile(profile: ProfileCreate):
    profile_obj = await Profile.create(**profile.dict())
    return profile_obj


@router.get("/profiles/", response_model=List[ProfileInResponse])
async def get_profiles():
    return await Profile.all()


@router.get("/profiles/{profile_id}", response_model=ProfileInResponse)
async def get_profile(profile_id: int):
    try:
        profile = await Profile.get(id=profile_id)
        return profile
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Profile not found")


@router.put("/profiles/{profile_id}", response_model=ProfileInResponse)
async def update_profile(profile_id: int, profile: ProfileUpdate):
    try:
        profile_obj = await Profile.get(id=profile_id)
        updated_profile = await profile_obj.update_from_dict(profile.dict(exclude_unset=True))
        await profile_obj.save()
        return updated_profile
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Profile not found")


@router.delete("/profiles/{profile_id}")
async def delete_profile(profile_id: int):
    try:
        profile = await Profile.get(id=profile_id)
        await profile.delete()
        return {"message": "Profile deleted successfully"}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Profile not found")


# Service Routes
@router.post("/services/", response_model=ServiceInResponse)
async def create_service(service: ServiceCreate):
    service_obj = await Service.create(**service.dict())
    return service_obj


@router.get("/services/", response_model=List[ServiceInResponse])
async def get_services():
    return await Service.all()


@router.get("/services/{service_id}", response_model=ServiceInResponse)
async def get_service(service_id: int):
    try:
        service = await Service.get(id=service_id)
        return service
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Service not found")


@router.put("/services/{service_id}", response_model=ServiceInResponse)
async def update_service(service_id: int, service: ServiceUpdate):
    try:
        service_obj = await Service.get(id=service_id)
        updated_service = await service_obj.update_from_dict(service.dict(exclude_unset=True))
        await service_obj.save()
        return updated_service
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Service not found")


@router.delete("/services/{service_id}")
async def delete_service(service_id: int):
    try:
        service = await Service.get(id=service_id)
        await service.delete()
        return {"message": "Service deleted successfully"}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Service not found")


# Skill Routes
@router.post("/skills/", response_model=SkillInResponse)
async def create_skill(skill: SkillCreate):
    skill_obj = await Skill.create(**skill.dict())
    return skill_obj


@router.get("/skills/", response_model=List[SkillInResponse])
async def get_skills():
    return await Skill.all()


@router.get("/skills/{skill_id}", response_model=SkillInResponse)
async def get_skill(skill_id: int):
    try:
        skill = await Skill.get(id=skill_id)
        return skill
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Skill not found")


@router.put("/skills/{skill_id}", response_model=SkillInResponse)
async def update_skill(skill_id: int, skill: SkillUpdate):
    try:
        skill_obj = await Skill.get(id=skill_id)
        updated_skill = await skill_obj.update_from_dict(skill.dict(exclude_unset=True))
        await skill_obj.save()
        return updated_skill
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Skill not found")


@router.delete("/skills/{skill_id}")
async def delete_skill(skill_id: int):
    try:
        skill = await Skill.get(id=skill_id)
        await skill.delete()
        return {"message": "Skill deleted successfully"}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Skill not found")


# Education Routes
@router.post("/educations/", response_model=EducationInResponse)
async def create_education(education: EducationCreate):
    education_obj = await Education.create(**education.dict())
    return education_obj


@router.get("/educations/", response_model=List[EducationInResponse])
async def get_educations():
    return await Education.all()


@router.get("/educations/{education_id}", response_model=EducationInResponse)
async def get_education(education_id: int):
    try:
        education = await Education.get(id=education_id)
        return education
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Education not found")


@router.put("/educations/{education_id}", response_model=EducationInResponse)
async def update_education(education_id: int, education: EducationUpdate):
    try:
        education_obj = await Education.get(id=education_id)
        updated_education = await education_obj.update_from_dict(education.dict(exclude_unset=True))
        await education_obj.save()
        return updated_education
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Education not found")


@router.delete("/educations/{education_id}")
async def delete_education(education_id: int):
    try:
        education = await Education.get(id=education_id)
        await education.delete()
        return {"message": "Education deleted successfully"}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Education not found")


# Employment Routes
@router.post("/employments/", response_model=EmploymentInResponse)
async def create_employment(employment: EmploymentCreate):
    employment_obj = await Employment.create(**employment.dict())
    return employment_obj


@router.get("/employments/", response_model=List[EmploymentInResponse])
async def get_employments():
    return await Employment.all()


@router.get("/employments/{employment_id}", response_model=EmploymentInResponse)
async def get_employment(employment_id: int):
    try:
        employment = await Employment.get(id=employment_id)
        return employment
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Employment not found")


@router.put("/employments/{employment_id}", response_model=EmploymentInResponse)
async def update_employment(employment_id: int, employment: EmploymentUpdate):
    try:
        employment_obj = await Employment.get(id=employment_id)
        updated_employment = await employment_obj.update_from_dict(employment.dict(exclude_unset=True))
        await employment_obj.save()
        return updated_employment
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Employment not found")


@router.delete("/employments/{employment_id}")
async def delete_employment(employment_id: int):
    try:
        employment = await Employment.get(id=employment_id)
        await employment.delete()
        return {"message": "Employment deleted successfully"}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Employment not found")


# Testimonial Routes
@router.post("/testimonials/", response_model=TestimonialInResponse)
async def create_testimonial(testimonial: TestimonialCreate):
    testimonial_obj = await Testimonial.create(**testimonial.dict())
    return testimonial_obj


@router.get("/testimonials/", response_model=List[TestimonialInResponse])
async def get_testimonials():
    return await Testimonial.all()


@router.get("/testimonials/{testimonial_id}", response_model=TestimonialInResponse)
async def get_testimonial(testimonial_id: int):
    try:
        testimonial = await Testimonial.get(id=testimonial_id)
        return testimonial
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Testimonial not found")


@router.put("/testimonials/{testimonial_id}", response_model=TestimonialInResponse)
async def update_testimonial(testimonial_id: int, testimonial: TestimonialUpdate):
    try:
        testimonial_obj = await Testimonial.get(id=testimonial_id)
        updated_testimonial = await testimonial_obj.update_from_dict(testimonial.dict(exclude_unset=True))
        await testimonial_obj.save()
        return updated_testimonial
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Testimonial not found")


@router.delete("/testimonials/{testimonial_id}")
async def delete_testimonial(testimonial_id: int):
    try:
        testimonial = await Testimonial.get(id=testimonial_id)
        await testimonial.delete()
        return {"message": "Testimonial deleted successfully"}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Testimonial not found")


# Portfolio Routes
@router.post("/portfolios/", response_model=PortfolioInResponse)
async def create_portfolio(portfolio: PortfolioCreate):
    portfolio_obj = await Portfolio.create(**portfolio.dict())
    return portfolio_obj


@router.get("/portfolios/", response_model=List[PortfolioInResponse])
async def get_portfolios():
    return await Portfolio.all()


@router.get("/portfolios/{portfolio_id}", response_model=PortfolioInResponse)
async def get_portfolio(portfolio_id: int):
    try:
        portfolio = await Portfolio.get(id=portfolio_id)
        return portfolio
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Portfolio not found")


@router.put("/portfolios/{portfolio_id}", response_model=PortfolioInResponse)
async def update_portfolio(portfolio_id: int, portfolio: PortfolioUpdate):
    try:
        portfolio_obj = await Portfolio.get(id=portfolio_id)
        updated_portfolio = await portfolio_obj.update_from_dict(portfolio.dict(exclude_unset=True))
        await portfolio_obj.save()
        return updated_portfolio
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Portfolio not found")


@router.delete("/portfolios/{portfolio_id}")
async def delete_portfolio(portfolio_id: int):
    try:
        portfolio = await Portfolio.get(id=portfolio_id)
        await portfolio.delete()
        return {"message": "Portfolio deleted successfully"}
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Portfolio not found")
