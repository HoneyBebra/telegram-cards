import asyncio

from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from core.config import settings

from bot.dispatcher.dispatcher import get_dispatcher


async def main() -> None:
    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    await get_dispatcher().start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
