from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

HELP_COMMAND = """
/help - список команд,
<em>/start - начать работу с ботом</em>
"""


router = Router()

@router.message(CommandStart())  
async def cmd_start(message: Message):
    await message.answer(
        "Are you satisfied with your work?",
    )

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        text = HELP_COMMAND, parse_mode="HTML"
    )