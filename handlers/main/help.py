from aiogram import types
from utils.api_connector import get_response_global

from loader import dp, storage, bot


@dp.message_handler(commands='help')
@dp.callback_query_handler(text='help')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    text = [
        '----------------------------------------------------------',
        '--------------*** Help Menu ***---------------',
        '----------------------------------------------------------',
        'Common commands: ',
        '/start - main menu',
        '/help - display this menu',
        '/about - learn about bot and developer',
        '----------------------------------------------------------',
        'Usable commands: ',
        '/world_stat - get global statistics about COVID-19',
        '/detailed_info - get detailed statistics',
        '/my_country - get COVID-19 statistics in your country',
        '/news - display latest new about COVID-19',
        '/faq - frequently asked questions'
    ]
    text = '\n'.join(text)

    await bot.delete_message(message.chat.id, message.from_user.id)
    await bot.send_message(query.from_user.id, text)

