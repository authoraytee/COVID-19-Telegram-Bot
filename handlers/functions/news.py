from aiogram import types
from utils.parser import parse

from loader import dp, storage, bot


@dp.message_handler(commands='news')
@dp.callback_query_handler(text='news')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    await bot.send_message(query.from_user.id, parse())
        

