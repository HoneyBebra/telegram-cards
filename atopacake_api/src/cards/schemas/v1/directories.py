from uuid import UUID

from src.common.schemas import BaseSchema


class DirectorySchema(BaseSchema):
    id: UUID
    user_id: UUID
    name: str
