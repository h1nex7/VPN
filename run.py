import os
import asyncio
from aiogram import Bot, Dispatcher

from dotenv import load_dotenv

from app.client import client


async def main():
    bot = Bot(token=os.getenv('TG_TOKEN'))
    dp = Dispatcher()
    dp.include_router(client)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
