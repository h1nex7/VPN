import os
import asyncio
from aiogram import Bot, Dispatcher

from dotenv import load_dotenv

from app.client import client
from app.database.models import init_models


async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('TG_TOKEN'))

    dp = Dispatcher()
    dp.include_router(client)
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)

    await dp.start_polling(bot)


async def startup(dispatcher: Dispatcher):
    await init_models()
    print('Бот запущен...')


async def shutdown(dispatcher: Dispatcher):
    print('Бот остановлен...')


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
