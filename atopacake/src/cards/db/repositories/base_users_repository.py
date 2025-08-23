from abc import ABC, abstractmethod
from uuid import UUID

from ...schemas.v1.users import UserSchema

# TODO: hash sensitive data!!


class BaseUsersRepository(ABC):
    """Abstract class describing working with database."""

    @abstractmethod
    async def create(
            self,
            login: str,
            password: str,
            phone_number: str | None = None,
    ) -> UserSchema:
        raise NotImplementedError

    @abstractmethod
    async def read(
            self,
            user_id: UUID,
    ) -> UserSchema:
        raise NotImplementedError

    @abstractmethod
    async def update(
            self,
            user_id: UUID,
            login: str | None = None,
            password: str | None = None,
            phone_number: str | None = None,
    ) -> UserSchema:
        raise NotImplementedError

    @abstractmethod
    async def delete(
            self,
            user_id: UUID,
    ) -> None:
        raise NotImplementedError
