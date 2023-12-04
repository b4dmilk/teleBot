from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.filters.state import StateFilter, StatesGroup, State
from keyboards.keyboards import get_main_kb
from aiogram.fsm.context import FSMContext

HELP_COMMAND = """
/help - список команд,
<em>/start - начать работу с ботом</em>
"""


router = Router()
class createNewProfile(StatesGroup):
    name = State()
    groups = State()

@router.message(CommandStart())  
async def cmd_start(message: Message):
    await message.answer(
        "Are you satisfied with your work?", reply_markup=get_main_kb()
    )

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        text = HELP_COMMAND, parse_mode="HTML"
    )

@router.message(StateFilter(None),Command("register"))
async def get_register(message:Message, state: FSMContext):
    await message.answer(
        text = "Hi, dear friend! What's your name?"
    )
    await state.set_state(createNewProfile.name)   

@router.message(createNewProfile.name, F.text)
async def remember_name(message:Message, state: FSMContext):
    await message.answer(
        text="Good. Enter groups."
    )
    await state.set_state(createNewProfile.groups)

@router.message(createNewProfile.groups, F.text)
async def remember_group(message: Message, state: FSMContext):
    await message.answer(
        text="The end🙃"
    )
    await state.clear()