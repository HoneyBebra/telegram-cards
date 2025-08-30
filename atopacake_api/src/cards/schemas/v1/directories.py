from uuid import UUID

from src.cards.schemas.v1.base import BaseSchema


class DirectorySchema(BaseSchema):
    id: UUID
    user_id: UUID
    name: str
