from uuid import UUID

from src.common.schemas import BaseSchema


class CardSchema(BaseSchema):
    id: UUID
    directory_id: UUID
    side_a: str
    side_b: str
    weight: float
