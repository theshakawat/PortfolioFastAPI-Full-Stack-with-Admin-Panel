from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import date

class BaseModelWithId(BaseModel):
    id: int


class ProfileBase(BaseModel):
    name: str
    job_title: str
    bio_title: str
    bio: str
    email: str
    phone: Optional[str] = None
    spoken_language: Optional[str] = None
    nationality: Optional[str] = None
    address: Optional[str] = None
    freelance: Optional[str] = None
    avatar_url: Optional[str] = None
    cv_url: Optional[str] = None


class ProfileCreate(ProfileBase):
    pass


class ProfileUpdate(ProfileBase):
    name: Optional[str] = None
    job_title: Optional[str] = None
    bio_title: Optional[str] = None
    bio: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    spoken_language: Optional[str] = None
    nationality: Optional[str] = None
    address: Optional[str] = None
    freelance: Optional[str] = None
    avatar_url: Optional[str] = None
    cv_url: Optional[str] = None


class ProfileInResponse(ProfileBase, BaseModelWithId):
    pass


class ServiceBase(BaseModel):
    title: str
    description: str
    icon_id: Optional[str] = None
    serial: Optional[int] = 0
    is_active: Optional[bool] = True


class ServiceCreate(ServiceBase):
    pass


class ServiceUpdate(ServiceBase):
    title: Optional[str] = None
    description: Optional[str] = None
    icon_id: Optional[str] = None
    serial: Optional[int] = None
    is_active: Optional[bool] = None


class ServiceInResponse(ServiceBase, BaseModelWithId):
    pass


class SkillBase(BaseModel):
    title: str
    percent: int
    is_active: Optional[bool] = True
    serial: Optional[int] = 0


class SkillCreate(SkillBase):
    pass


class SkillUpdate(SkillBase):
    title: Optional[str] = None
    percent: Optional[int] = None
    is_active: Optional[bool] = None
    serial: Optional[int] = None


class SkillInResponse(SkillBase, BaseModelWithId):
    pass


class EducationBase(BaseModel):
    degree: str
    from_date: Optional[date] = None
    to_date: Optional[date] = None
    organization_name: str
    location: str
    website: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = True
    is_present: Optional[bool] = False


class EducationCreate(EducationBase):
    pass


class EducationUpdate(EducationBase):
    degree: Optional[str] = None
    from_date: Optional[date] = None
    to_date: Optional[date] = None
    organization_name: Optional[str] = None
    location: Optional[str] = None
    website: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None
    is_present: Optional[bool] = None


class EducationInResponse(EducationBase, BaseModelWithId):
    pass


class EmploymentBase(BaseModel):
    position: str
    from_date: Optional[date] = None
    to_date: Optional[date] = None
    organization_name: str
    location: Optional[str] = None
    website: Optional[str] = None
    responsibilities: str
    achievement: Optional[str] = None
    is_active: Optional[bool] = True
    is_present: Optional[bool] = False


class EmploymentCreate(EmploymentBase):
    pass


class EmploymentUpdate(EmploymentBase):
    position: Optional[str] = None
    from_date: Optional[date] = None
    to_date: Optional[date] = None
    organization_name: Optional[str] = None
    location: Optional[str] = None
    website: Optional[str] = None
    responsibilities: Optional[str] = None
    achievement: Optional[str] = None
    is_active: Optional[bool] = None
    is_present: Optional[bool] = None


class EmploymentInResponse(EmploymentBase, BaseModelWithId):
    pass


class TestimonialBase(BaseModel):
    quote_owner: str
    role: str
    quote: str
    is_active: Optional[bool] = True
    serial: Optional[int] = 0


class TestimonialCreate(TestimonialBase):
    pass


class TestimonialUpdate(TestimonialBase):
    quote_owner: Optional[str] = None
    role: Optional[str] = None
    quote: Optional[str] = None
    is_active: Optional[bool] = None
    serial: Optional[int] = None


class TestimonialInResponse(TestimonialBase, BaseModelWithId):
    pass


class PortfolioBase(BaseModel):
    type: Optional[str] = None
    title: str
    description: Optional[str] = None
    client: Optional[str] = None
    image_url: Optional[str] = None
    is_open_source: Optional[bool] = False
    technology: Optional[str] = None
    is_active: Optional[bool] = True
    serial: Optional[int] = 0
    project_url: Optional[str] = None


class PortfolioCreate(PortfolioBase):
    pass


class PortfolioUpdate(PortfolioBase):
    type: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    client: Optional[str] = None
    image_url: Optional[str] = None
    is_open_source: Optional[bool] = None
    technology: Optional[str] = None
    is_active: Optional[bool] = None
    serial: Optional[int] = None
    project_url: Optional[str] = None

class PortfolioInResponse(PortfolioBase, BaseModelWithId):
    pass

class EmailSchema(BaseModel):
    name: str
    email: EmailStr
    subject: str
    message: str