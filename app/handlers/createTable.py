from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.filters.state import StateFilter, StatesGroup, State
from aiogram.fsm.context import FSMContext
from database.db import create_table

router = Router()

class createNewTable(StatesGroup):
    name = State()

@router.message(Command("createTable"))
async def add_table(message: Message, state: FSMContext):
    await message.answer(
         text= "Enter table's name"
    )
    await state.set_state(createNewTable.name)

@router.message(createNewTable.name, F.text)
async def add_name(message: Message, state: FSMContext):
    data = await state.get_data()
    data['name'] = message.text
    await state.set_data(data)
    await create_table(state)
    await message.answer(
        text="Create table is successfully"
    )