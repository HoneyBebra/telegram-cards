from uuid import UUID, uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ...auth.models.users import Users
from ...cards.models.cards import Cards
from ...global_models.base import BaseModel


class Texts(BaseModel):
    __tablename__ = "texts"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
        unique=True,
        nullable=False,
    )
    text: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    user: Mapped["Users"] = relationship(
        "Users",
        back_populates="texts",
    )
    cards: Mapped[list["Cards"]] = relationship(
        "Cards",
        back_populates="text",
    )
