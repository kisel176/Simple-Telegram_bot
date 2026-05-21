from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import keyboards as kb

user = Router()

@user.message(CommandStart())
async def cmd_message(message: Message):
    await message.answer("Hello",
                         reply_markup=kb.menu)

@user.message(F.text == 'Каталог')
async def echo(message: Message):
    await message.answer('Privit',
                         reply_markup=kb.catalog)

@user.callback_query(F.data == 'Oi')
async def oi_callback(callback: CallbackQuery):
    await callback.answer('Butcher core')
    await callback.message.answer('Cunt!')

@user.message()
async def handle_start(message: Message):
    await message.send_copy(chat_id=message.from_user.id)
