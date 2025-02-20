import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import TELEGRAM_API_TOKEN
from search import torrent_search

# Setting up logging
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Welcome to the Torrent Search Bot! Use /search <keyword> to search for torrents.")

@dp.message_handler(commands=['search'])
async def handle_search(message: types.Message):
    await torrent_search(message)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
