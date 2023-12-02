import asyncio
from aiogram import Dispatcher
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from handlers import handlers

# launching bot
async def main():
    load_dotenv('.env')  
    token = os.getenv("TOKEN_API")
    bot = Bot(token)
    dp = Dispatcher()
    dp.include_routers(handlers.router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())