from uuid import UUID

from .base import BaseSchema


class UserSchema(BaseSchema):
    id: UUID
    login: str
    password: str
    phone_number: str
