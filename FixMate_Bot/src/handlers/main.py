import datetime

import aiosqlite
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from src import keyboards as kb

user = Router()

async def database(telegram_id, username) -> None:
    async with aiosqlite.connect('tz.db') as db:
        await db.execute("CREATE TABLE IF NOT EXISTS users (telegram_id BIGINT, username TEXT, date TEXT)")
        cursor = await db.execute("SELECT * FROM users WHERE telegram_id = ?", (telegram_id,))
        row = await cursor.fetchone()
        if row is not None:
            print("None")
            return
    date = f'{datetime.date.today()}'
    async with aiosqlite.connect('tz.db') as db:
        await db.execute("INSERT INTO users (telegram_id, username, date) VALUES (?, ?, ?)",
                         (telegram_id, username, date))
        await db.commit()

@user.message(CommandStart())
async def cmd_message(message: Message) -> None:
    await message.answer("Привет", reply_markup=kb.start)
    telegram_id = message.from_user.id
    username = message.from_user.username
    await database(telegram_id, username)