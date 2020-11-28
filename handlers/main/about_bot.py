from aiogram import types
from utils.api_connector import get_response_global

from loader import dp, storage, bot


@dp.message_handler(commands='about')
@dp.callback_query_handler(text='about')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    text = [
        '----------------------------------------------------------',
        '---------------*** About Bot ***----------------',
        '----------------------------------------------------------',
        'Здесь будет инормация о боте (не nelp)'
    ]
    text = '\n'.join(text)

    await bot.send_message(query.from_user.id, text)
