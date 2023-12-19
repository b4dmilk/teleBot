from aiogram import Router, F
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.filters.state import StateFilter, StatesGroup, State
from keyboards.keyboards import get_main_kb
from aiogram.fsm.context import FSMContext
from database.db import create_article

router = Router()



class createNewArticle(StatesGroup):
    name = State()
    desc = State()
    article = State()


@router.message(StateFilter(None), Command("addArticle"))
async def add_article(message: Message, state: FSMContext):
   # await create_article(user.id=messge.from_user.id)
   await message.answer(
      text= "Enter article's name"
   )
   await state.set_state(createNewArticle.name)

@router.message(createNewArticle.name, F.text)
async def add_name(message: Message, state: FSMContext):
    await message.answer(
        text="Descrioption pls."
    )
    data = await state.get_data()
    data['name'] = message.text
    await state.set_data(data)
    await state.set_state(createNewArticle.desc)

@router.message(createNewArticle.desc, F.text)
async def add_name(message: Message, state: FSMContext):
    await message.answer(
        text="ARTICLE"
    )
    data = await state.get_data()
    data['desc'] = message.text
    await state.set_data(data)
    await state.set_state(createNewArticle.article)

@router.message(createNewArticle.article, F.text)
async def add_name(message: Message, state: FSMContext):
    await message.answer(
        text="Good"
    )
    data = await state.get_data()
    data['article'] = message.text
    await state.set_data(data)
    await create_article(state, user_id=message.from_user.id)
    
   
    await message.answer( text=f"<b>{data['name']}</b>\n {data['desc']}\n{data['article']}", parse_mode= "HTML")
    await state.clear()


