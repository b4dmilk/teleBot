from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types.web_app_info import WebAppInfo
def get_main_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="/register")
    kb.button(text="/help")
    kb.button(text="About Me")
    kb.button(text="/addArticle")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True,input_field_placeholder="What you want?")

 
