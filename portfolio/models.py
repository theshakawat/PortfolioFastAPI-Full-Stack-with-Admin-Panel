from tortoise.models import Model
from tortoise import fields


class Profile(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=200)
    job_title = fields.CharField(max_length=200)
    bio_title = fields.CharField(max_length=500)
    bio = fields.TextField()
    email = fields.CharField(max_length=200, unique=True, null=True)
    phone = fields.CharField(max_length=50, default="", null=True)
    spoken_language = fields.CharField(max_length=200, default="", null=True)
    nationality = fields.CharField(max_length=200, default="", null=True)
    address = fields.CharField(max_length=200, default="", null=True)
    freelance = fields.CharField(max_length=200, default="", null=True)
    avatar_url = fields.CharField(max_length=500, default="", null=True)
    cv_url = fields.CharField(max_length=500, default="", null=True)

    class Meta:
        table = "profile"


class Service(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=200, unique=True)
    description = fields.TextField()
    icon_id = fields.CharField(max_length=200, null=True)
    serial = fields.IntField(unique=True, default=0)
    is_active = fields.BooleanField(default=True)

    class Meta:
        table = "service"


class Skill(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=200, unique=True)
    percent = fields.IntField()
    is_active = fields.BooleanField(default=True)
    serial = fields.IntField(unique=True, default=0)

    class Meta:
        table = "skill"


class Education(Model):
    id = fields.IntField(pk=True)
    degree = fields.CharField(max_length=200)
    from_date = fields.DateField(null=True)
    to_date = fields.DateField(null=True)
    organization_name = fields.CharField(max_length=200)
    location = fields.CharField(max_length=200)
    website = fields.CharField(max_length=500, null=True)
    description = fields.TextField(null=True)
    is_active = fields.BooleanField(default=True)
    is_present = fields.BooleanField(default=False)

    class Meta:
        table = "education"


class Employment(Model):
    id = fields.IntField(pk=True)
    position = fields.CharField(max_length=200)
    from_date = fields.DateField(null=True)
    to_date = fields.DateField(null=True)
    organization_name = fields.CharField(max_length=200)
    location = fields.CharField(max_length=200, null=True)
    website = fields.CharField(max_length=500, null=True)
    responsibilities = fields.TextField()
    achievement = fields.TextField(null=True)
    is_active = fields.BooleanField(default=True)
    is_present = fields.BooleanField(default=False)

    class Meta:
        table = "employment"


class Testimonial(Model):
    id = fields.IntField(pk=True)
    quote_owner = fields.CharField(max_length=200)
    role = fields.CharField(max_length=200)
    quote = fields.TextField()
    is_active = fields.BooleanField(default=True)
    serial = fields.IntField(unique=True, default=0)

    class Meta:
        table = "testimonial"


class Portfolio(Model):
    id = fields.IntField(pk=True)
    type = fields.CharField(max_length=200, null=True)
    title = fields.CharField(max_length=200)
    description = fields.TextField(null=True)
    client = fields.CharField(max_length=200, null=True)
    image_url = fields.CharField(max_length=500, null=True)
    is_open_source = fields.BooleanField(default=False)
    technology = fields.CharField(max_length=500, null=True)
    is_active = fields.BooleanField(default=True)
    serial = fields.IntField(unique=True, default=0)
    project_url = fields.CharField(max_length=500, null=True)

    class Meta:
        table = "portfolio"