from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery


client = Router()


@client.callback_query('back_to_main')
@client.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello')
