from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from app.database.requests import set_user


client = Router()


# @client.callback_query('back_to_main')
@client.message(CommandStart())
async def cmd_start(message: Message):
    is_user = await set_user(message.from_user.id)
    if is_user:
        await message.answer(f'Рады снова видеть вас {message.from_user.first_name}')
    else:
        await message.answer('Пройди регистрацию')
