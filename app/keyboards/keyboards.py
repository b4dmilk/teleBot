from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_main_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="/register")
    kb.button(text="/help")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True,input_field_placeholder="What you want?")

 
