from aiogram import types
from utils.api_connector import get_response_global

from loader import dp, storage, bot


@dp.message_handler(commands='world_stat')
@dp.callback_query_handler(text='world_stat')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):

    stat = get_response_global('all')
    cases = stat['cases']
    recovered = stat['recovered']
    active = stat['active']
    deaths = stat['deaths']


    await bot.send_message(query.from_user.id, 
    'COVID-19 Global Stats:\n\
---------------------------------------------------------------------\n\
* Statistics Are Updated Every 10 Minutes *\n\
---------------------------------------------------------------------\n\
Total Cases - {}\n\
Total Recovered - {}\n\
Active Cases - {}\n\
Total Deaths - {}\n\
------------------------------------------------\n\
    '.format(cases, recovered, active, deaths)
    )