from uuid import UUID, uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel
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

    directory: Mapped["Directories"] = relationship(
        "Directories",
        back_populates="directory",
    )
