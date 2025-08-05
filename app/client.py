from aiogram import Router, F
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.database.requests import set_user
import app.keyboard as kb
from app.states import RegStates


client = Router()


@client.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    is_user = await set_user(message.from_user.id)
    if is_user:
        await message.answer(f'Рады снова видеть вас {message.from_user.first_name}')
    else:
        await message.answer(f'Привет {message.from_user.first_name}\n\nЧтобы продолжить нажми на кнопкe снизу',
                             reply_markup=kb.connect_register)
        await state.set_state(RegStates.reg_first)


@client.callback_query(F.data == 'connected')
async def start_registration(callback: CallbackQuery, state: FSMContext):
    await state.set_state(RegStates.choose_device)  # <-- поменяли состояние
    await callback.message.answer(
        "🎉 Поздравляем! Вы зарегистрировали аккаунт OkayVPN.\n\n"
        "Теперь настроим ваш VPN! Выберите устройство, на котором хотите использовать VPN:",
        reply_markup=kb.devices_kb
    )
    await callback.answer()


@client.callback_query(StateFilter(RegStates.choose_device), F.data.startswith("device_"))
async def choose_device(callback: CallbackQuery, state: FSMContext):
    device = callback.data.split("_")[1]
    await state.update_data(device=device)

    await state.clear()

    if device == "ios":
        instruction = "📖 Инструкция по настройке для iOS: ..."
    elif device == "android":
        instruction = "📖 Инструкция по настройке для Android: ..."
    elif device == "macos":
        instruction = "📖 Инструкция по настройке для MacOS: ..."
    else:
        instruction = "📖 Инструкция по настройке для Windows: ..."

    await callback.message.answer(instruction)
    await callback.answer()


@client.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Пока здесь ничего нет')
