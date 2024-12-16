import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
import asyncio

API_TOKEN = 'BOT_TOKEN'  # Замените на ваш токен

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание объекта бота
bot = Bot(token=API_TOKEN)

# Создание экземпляра Dispatcher
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.message()
async def all_messages(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')

async def main():
    # Запускаем бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())



