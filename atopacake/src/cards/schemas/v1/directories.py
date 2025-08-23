from uuid import UUID

from .base import BaseSchema


class DirectorySchema(BaseSchema):
    id: UUID
    user_id: UUID
    name: str
