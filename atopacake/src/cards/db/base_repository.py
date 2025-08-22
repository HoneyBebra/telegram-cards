from abc import ABC, abstractmethod
from uuid import UUID


class Repository(ABC):
    """Abstract class describing working with database."""

    @abstractmethod
    async def create_card(
            self,
            directory_id: UUID,
            side_a: str,
            side_b: str,
    ) -> CardSchema:
        raise NotImplementedError
