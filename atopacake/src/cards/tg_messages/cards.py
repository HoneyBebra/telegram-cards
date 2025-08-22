from aiogram import F
from aiogram.types import Message
from core.config import commands

from ..tg_dispatcher.dispatcher import get_dispatcher

dp = get_dispatcher()


@dp.message(F.text == commands.add_card_command)
async def add_card_handler(message: Message) -> None:
    await message.answer("Логика добавления карточки")


@dp.message(F.text == commands.learn_cards_command)
async def learn_card_handler(message: Message) -> None:
    await message.answer("Логика учения карточек")


def init_cards() -> bool:
    return True
