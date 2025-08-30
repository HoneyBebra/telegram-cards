from uuid import UUID, uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ...global_models.base import BaseModel
from ...texts.models.texts import Texts
from .directories import Directories


class Cards(BaseModel):
    __tablename__ = "cards"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
        unique=True,
        nullable=False,
    )
    directory_id: Mapped[UUID] = mapped_column(
        ForeignKey("directories.id"),
        nullable=False,
    )
    side_a: Mapped[str] = mapped_column(nullable=False)
    side_b: Mapped[str] = mapped_column(nullable=False)
    weight: Mapped[float] = mapped_column(default=0.5)
    random_mix_sides: Mapped[bool] = mapped_column(default=False)
    text_id: Mapped[UUID] = mapped_column(
        ForeignKey("texts.id"),
        nullable=True
    )
    text_offset: Mapped[int] = mapped_column(nullable=True)

    directory: Mapped["Directories"] = relationship(
        "Directories",
        back_populates="cards",
    )
    text: Mapped["Texts"] = relationship(
        "Texts",
        back_populates="cards",
    )
