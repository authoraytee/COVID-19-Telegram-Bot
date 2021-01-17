import logging
from aiogram import types

from loader import dp, storage, bot
import keyboards.start_keyboard as kb


@dp.message_handler(commands=['start'])
async def start(message: types.Message):

    text = 'Welcome to COVID-19 bot \n\
---------------------------------------------------------\n\
Select the function you are interested in: '

    await message.reply(text, reply_markup=kb.inline_kb_full)