from aiogram import types
from loader import dp, storage, bot

from utils.database import get_answer, get_questions

from aiogram.types import CallbackQuery


@dp.message_handler(commands=['faq'])
@dp.callback_query_handler(text='faq')
async def faq(query: types.CallbackQuery):

    text = [get_questions()]
    text = '\n'.join(text)

    await bot.send_message(query.from_user.id, text)



commands = []
for i in range(15):
    commands.append('FAQ_{}'.format(i+1))

@dp.message_handler(commands=commands)
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):

    question_number = query.text[-2::]
    if question_number[0] == "_":
        question_number = command_number[-1]

    await bot.send_message(query.from_user.id, get_answer(question_number))
