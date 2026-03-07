from pydantic import BaseModel


class Lead(BaseModel):

    name: str | None = None
    role: str | None = None
    company: str | None = None
    website: str | None = None
    linkedin: str | None = None
    email: str | None = None