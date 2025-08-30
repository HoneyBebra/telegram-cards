from abc import ABC, abstractmethod
from uuid import UUID

from ....schemas.v1.cards import CardSchema


class BaseCardsRepository(ABC):
    """Abstract class describing working with database."""

    @abstractmethod
    async def create(
            self,
            directory_id: UUID,
            side_a: str,
            side_b: str,
            random_mix_sides: bool = False,
            text_id: UUID | None = None,
            text_offset: int | None = None,
    ) -> CardSchema:
        raise NotImplementedError

    @abstractmethod
    async def read_n_random(self, n_count: int, directory_id: UUID) -> list[CardSchema]:
        raise NotImplementedError

    @abstractmethod
    async def update(
            self,
            card_id: UUID,
            directory_id: UUID | None = None,
            side_a: str | None = None,
            side_b: str | None = None,
            random_mix_sides: bool | None = None,
    ) -> CardSchema:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, card_id: UUID) -> None:
        raise NotImplementedError
