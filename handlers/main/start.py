import logging
from aiogram import types

from loader import dp, storage, bot


@dp.message_handler(commands='start')
async def start_cmd_handler(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=1)
    keyboard_markup.add(
        types.InlineKeyboardButton('1. Global Stats', callback_data='world_stat'),
        types.InlineKeyboardButton('2. Detailed info', callback_data='detailed_info'),
        types.InlineKeyboardButton('3. Latest news', callback_data='news'),
        types.InlineKeyboardButton('4. TOP-20', callback_data='top_20'),
        types.InlineKeyboardButton('5. My Country', callback_data='my_country'),
        types.InlineKeyboardButton('--- Get Help ---', callback_data='help'),
        types.InlineKeyboardButton('--- About Bot ---', callback_data='about'),
        types.InlineKeyboardButton('--- FAQ ---', callback_data='faq'),
    )
    text = 'Welcome to COVID-19 bot \n---------------------------------------------------------\nSelect the function you are interested in: '

    await message.reply(text, reply_markup=keyboard_markup)

