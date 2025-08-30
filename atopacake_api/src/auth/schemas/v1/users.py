from uuid import UUID

from src.auth.schemas.v1.base import BaseSchema


class UserSchema(BaseSchema):
    id: UUID
    login: str
    password: str
    phone_number: str
