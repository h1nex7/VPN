from aiogram.types import reply_keyboard_markup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


connect_register = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🎉Подключить🎉', callback_data='connected')]
])
