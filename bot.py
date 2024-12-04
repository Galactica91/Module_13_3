from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "7775779452:AAEATs0Fe0bP-tyd7DfnOmL3nOPUGEWIEI4"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['Start'])
async def command_start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")

@dp.message_handler()
async def all_messages(message):
    await message.answer("Введите команду /start, чтобы начать общение")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
