from uuid import UUID

from .base import BaseSchema


class TgUserSchema(BaseSchema):
    user_id: UUID
    tg_id: UUID
    username: str
