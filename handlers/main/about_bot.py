from aiogram import types
from utils.api_connector import get_response_global

from loader import dp, storage, bot


@dp.message_handler(commands='about')
@dp.callback_query_handler(text='about')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):

    dashed_line = '-'*57

    text = [
        dashed_line,
        '---------------*** About Bot ***----------------',
        dashed_line,

        'Hello! This is a telegram bot that will show you up-to-date\
 information about the COVID-19 in different countries and\
 specifically in yours, tell you about the latest\
 news related to the virus and explain what a coronavirus is\
 and what to do with it!\n',

        'You can get more about commands and functions using the "Get Help" menu\n',

        'If you want to know what technologies were used or look at the code\
 or make a couple of code improvement recommendations or\
 new feature suggestions to me - it\'s on my GitHub repository\n',

        dashed_line,

        'Author: github.com/authoraytee',
        'Source code: github.com/authoraytee/COVID-19-Telegram-Bot',

        dashed_line,

        'Used resources:',
        'API I used for global and detailed informattion: disease.sh/',
        'Latest news resource: covid-stat.com/',
        'Where did I get the information for my FAQ: www.who.int/\n',

        'THANKS FOR USING COVID-19 SUPER ULTRA BOT!!!!'
    ]
    text = '\n'.join(text)

    await bot.send_message(query.from_user.id, text)
