from uuid import UUID

from src.common.schemas import BaseSchema


class UserSchema(BaseSchema):
    id: UUID
    login: str
    password: str
    phone_number: str
