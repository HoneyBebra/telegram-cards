from uuid import UUID, uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel
from .cards import Cards
from .users import Users


class Directories(BaseModel):
    __tablename__ = "directories"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
        unique=True,
        nullable=False,
    )
    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )
    name: Mapped[str] = mapped_column(nullable=False)

    user: Mapped["Users"] = relationship(
        "Users",
        back_populates="directories",
    )
    cards: Mapped[list["Cards"]] = relationship(
        "Cards",
        back_populates="cards",
    )
