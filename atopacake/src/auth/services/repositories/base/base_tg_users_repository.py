# Maybe this will be moved to the auth service

from abc import ABC, abstractmethod
from uuid import UUID

from ....schemas.v1.tg_users import TgUserSchema

# TODO: hash sensitive data!!


class BaseTgUsersRepository(ABC):
    """Abstract class describing working with database."""

    @abstractmethod
    async def create(
            self,
            tg_id: int,
            username: str,
            user_id: UUID | None = None,
    ) -> TgUserSchema:
        raise NotImplementedError

    @abstractmethod
    async def read(self, user_id: UUID) -> TgUserSchema:
        raise NotImplementedError

    @abstractmethod
    async def update(self, tg_id: int, username: str) -> TgUserSchema:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, user_id: UUID) -> None:
        raise NotImplementedError
