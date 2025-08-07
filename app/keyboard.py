from aiogram.types import reply_keyboard_markup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


connect_register = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🎉Подключить🎉', callback_data='connected')]
])

devices_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='📱 iOS (iPhone, iPad)',
                          callback_data='device_ios')],
    [InlineKeyboardButton(text='📱 Android', callback_data='device_android')],
    [InlineKeyboardButton(text='💻 MacOS', callback_data='device_macos')],
    [InlineKeyboardButton(text='💻 Windows', callback_data='device_windows')]
])


after_reg = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='📱 Мои устройтва 💻', callback_data='devices')],
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='back_to_main')]
])


main_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='📱 Мои устройтва 💻', callback_data='devices')],
    [InlineKeyboardButton(text='Пригласить друга', callback_data='invite'),
     InlineKeyboardButton(text='Помощь 📖', callback_data='help')]
])


help_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🏠 Главное меню', callback_data='back_to_main')]
])
