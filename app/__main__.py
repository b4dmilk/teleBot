import asyncio
from aiogram import Dispatcher
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from handlers import commandHandlers, other
from database.db import db_start



async def on_startup():
    await db_start()

# launching bot
async def main():
    load_dotenv('.env')  
    token = os.getenv("TOKEN_API")
    bot = Bot(token)
    dp = Dispatcher()
    dp.include_routers(commandHandlers.router, other.router)
    await on_startup()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    


if __name__ == "__main__":
    asyncio.run(main())