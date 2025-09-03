from uuid import UUID

from src.common.schemas import BaseSchema


class TgUserSchema(BaseSchema):
    user_id: UUID
    tg_id: UUID
    username: str
