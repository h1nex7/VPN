from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from app.database.requests import set_user
import app.keyboard as kb

client = Router()


@client.callback_query(F.data == 'back_to_main')
@client.message(CommandStart())
async def cmd_start(message: Message):
    is_user = await set_user(message.from_user.id)
    if not is_user:
        await message.answer(f'Привет {message.from_user.first_name}\n\nЧтобы продолжить нажми на кнопкe снизу',
                             reply_markup=kb.connect_register)
    else:
        await message.answer(f'Рады снова видеть вас {message.from_user.first_name}')


@client.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Пока здесь ничего нет')
