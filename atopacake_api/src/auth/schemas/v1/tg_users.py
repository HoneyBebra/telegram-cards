from uuid import UUID

from src.auth.schemas.v1.base import BaseSchema


class TgUserSchema(BaseSchema):
    user_id: UUID
    tg_id: UUID
    username: str
