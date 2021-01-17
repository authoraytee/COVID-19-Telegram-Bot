from aiogram import types
from utils.api_connector import top

from loader import dp, storage, bot


@dp.message_handler(commands='top_20')
@dp.callback_query_handler(text='top_20')
async def top_20(query: types.CallbackQuery):
 
    total_cases = top(20, 'cases')
    message = '-'*20 + ' Total cases ' + '-'*20 + '\n\n'
    for i in total_cases:
        message = message + i + '\n'


    await bot.send_message(query.from_user.id, message)