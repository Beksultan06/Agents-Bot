from aiogram import Bot, types, Dispatcher
from aiogram.filters import Command
import asyncio, logging, os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.environ.get("token"))
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message:types.Message):
    await message.answer("Привет я бот который предоставляет Агентов!")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())