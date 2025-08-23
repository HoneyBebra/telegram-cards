from uuid import UUID

from .base import BaseSchema


class CardSchema(BaseSchema):
    id: UUID
    directory_id: UUID
    side_a: str
    side_b: str
    weight: float
