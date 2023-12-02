from aiogram import Dispatcher
from aiogram.utils import executor
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types


load_dotenv('.env')  
token = os.getenv("TOKEN_API")
bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
        await bot.send_message(chat_id=message.from_user.id,text='Hi')
        await message.delete()


if __name__ == '__main__':
    executor.start_polling(
        dp, skip_updates=True
    )

