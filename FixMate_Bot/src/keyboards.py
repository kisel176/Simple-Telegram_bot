from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Загрузить пример отчёта', callback_data='upload_report')],
        [InlineKeyboardButton(text='Об проекте', callback_data='ob_proekte'),
        InlineKeyboardButton(text='Поддержать авторов', callback_data='podderzat_avtorov')],
        [InlineKeyboardButton(text='Создать новый отчёт', switch_inline_query_current_chat="/new_report")],
    ]
)