from aiogram.types import reply_keyboard_markup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


connect_register = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🎉Подключить🎉', callback_data='connected')]
])

devices_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📱 iOS (iPhone, iPad)",
                          callback_data="device_ios")],
    [InlineKeyboardButton(text="📱 Android", callback_data="device_android")],
    [InlineKeyboardButton(text="💻 MacOS", callback_data="device_macos")],
    [InlineKeyboardButton(text="💻 Windows", callback_data="device_windows")],
])
