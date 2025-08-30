from uuid import UUID, uuid4

from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.auth.models.tg_users import TgUsers
from src.cards.models.directories import Directories
from src.global_models.base import BaseModel
from src.texts.models.texts import Texts


class Users(BaseModel):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
        unique=True,
        nullable=False,
    )
    login: Mapped[str] = mapped_column(nullable=True)
    password: Mapped[str] = mapped_column(nullable=True)
    phone_number: Mapped[str] = mapped_column(nullable=True)

    tg_user: Mapped["TgUsers"] = relationship(
        "TgUsers",
        back_populates="user",
        uselist=False,  # One to one
    )
    directories: Mapped[list["Directories"]] = relationship(
        "Directories",
        back_populates="user",
    )
    texts: Mapped[list["Texts"]] = relationship(
        "Texts",
        back_populates="user",
    )

    # TODO:
    # def check_password(self, password: str) -> bool:
    #     return check_password_hash(self.password, password)
