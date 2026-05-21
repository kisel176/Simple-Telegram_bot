from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Меню')],
        [KeyboardButton(text='Каталог'),
        KeyboardButton(text='Contacts')]
    ],
    resize_keyboard = True,
    input_field_placeholder='Make your choice'
)

catalog = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Nikto', url='https://t.me/nicktonik0')],
        [InlineKeyboardButton(text='Oi', callback_data='Oi'),
        InlineKeyboardButton(text='SUS', url='https://t.me/nicktonik0')]
    ]
)