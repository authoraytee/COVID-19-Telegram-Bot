from aiogram import types
from loader import dp, storage, bot

from utils.database import connect

@dp.message_handler(commands='faq')
@dp.callback_query_handler(text='faq')
async def start_cmd_handler(message: types.Message):

    keyboard_markup = types.InlineKeyboardMarkup(row_width=1)
    keyboard_markup.add(
        types.InlineKeyboardButton('1. What is COVID-19?', callback_data='rer1'),
        types.InlineKeyboardButton('2. What are the symptoms of COVID-19?', callback_data='rer2'),
        types.InlineKeyboardButton('3. What happens to people who get COVID-19?', callback_data='rer3'),
        types.InlineKeyboardButton('4. Who is most at risk of severe illness from COVID-19?', callback_data='rer4'),
    )
    text = '----- Frequently Asked Questions -----'
    await message.reply(text, reply_markup=keyboard_markup)


@dp.callback_query_handler(text='rer1')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    await bot.send_message(query.from_user.id, connect(1))

@dp.callback_query_handler(text='rer2')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    await bot.send_message(query.from_user.id, connect(2))

@dp.callback_query_handler(text='rer3')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    await bot.send_message(query.from_user.id, connect(3))

@dp.callback_query_handler(text='rer4')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    await bot.send_message(query.from_user.id, connect(4))