from aiogram import types
from aiogram.filters import CommandStart
from core.config import commands

from ..tg_dispatcher.dispatcher import get_dispatcher

dp = get_dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    keyboard_buttons = [
        [types.KeyboardButton(text=commands.add_card_command)],
        [types.KeyboardButton(text=commands.learn_cards_command)],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=keyboard_buttons)
    await message.answer("Привет! Это бот с карточками для изучения", reply_markup=keyboard)


def init_registration() -> bool:
    return True
