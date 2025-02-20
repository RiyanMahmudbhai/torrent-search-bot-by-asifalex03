import logging
from aiogram import Bot, Dispatcher, types
from config import TELEGRAM_API_TOKEN
from search import torrent_search

# Setting up logging
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    # No need to import ParseMode, just use types.ParseMode directly
    await message.reply("Welcome to the Torrent Search Bot! Use /search <keyword> to search for torrents.")

@dp.message_handler(commands=['search'])
async def handle_search(message: types.Message):
    await torrent_search(message)

# Start polling with the new method for aiogram v3.x
async def on_start():
    await dp.start_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(on_start())
