from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.filters.state import StateFilter, StatesGroup, State
from aiogram.fsm.context import FSMContext
from database.db import create_article
#from keyboards.inlineKeyboards import cmd_random, get_inline_keyboard
from aiogram.types.web_app_info import WebAppInfo



router = Router()

ABOUT = """Hi, my dear friend! 
        It's my contacts: 
"""
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import Message

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

@router.message(F.text == "About Me")
async def about_info(message: Message):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(
        text="GitHub",  
        web_app=WebAppInfo(url="https://github.com/b4dmilk"),)
        )
    builder.row(InlineKeyboardButton(
        text="Оф. канал Telegram",
        url="https://t.me/badmi1k")
    )
    await message.answer(
    text=ABOUT, parse_mode="HTML", reply_markup=builder.as_markup(),
     )
  