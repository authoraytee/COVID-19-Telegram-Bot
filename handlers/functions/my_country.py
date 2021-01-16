from aiogram import types
from utils.api_connector import my_country

from loader import dp, storage, bot


@dp.message_handler(commands='my_country')
@dp.callback_query_handler(text='my_country')
async def my_country_handler(query: types.CallbackQuery):

    # Telegram does not let you know the user's country for security reasons, 
    # so you can only use the language
    user_lang = query.from_user.language_code

    if user_lang == 'en':
            await bot.send_message(query.from_user.id, english_lan_handler())
    else: 
        try: 
            stat = my_country(user_lang)

            await bot.send_message(query.from_user.id, handler_body(stat))
            
        except Error as e:
            await bot.send_message(query.from_user.id, 'There was an error getting info!')


def english_lan_handler():
    return 'Your account language in english so country can\'t be identified!\n\
But if you really want to, you can find it on covid-stat.com/ or any else source!'


def handler_body(stat):
    country = stat['country']
    population = stat['population']
    cases = stat['cases']
    tests = stat['tests']
    recovered = stat['recovered']
    active = stat['active']
    critical = stat['critical']
    deaths = stat['deaths']

    todayCases = stat['todayCases']
    todayRecovered = stat['todayRecovered']

    casesPerOneMillion = stat['casesPerOneMillion']
    testsPerOneMillion = stat['testsPerOneMillion']
    activePerOneMillion = stat['activePerOneMillion']
    recoveredPerOneMillion = stat['recoveredPerOneMillion']
    criticalPerOneMillion = stat['criticalPerOneMillion']
    deathsPerOneMillion = stat['deathsPerOneMillion']

    return 'COVID-19 in your country:\n\
---------------------------------------------------------------------\n\
* Statistics Are Updated Every 10 Minutes *\n\
---------------------------------------------------------------------\n\
---*** Your Country - {} ***---\n\
---------------------------------------------------------------------\n\
----- Main information -----\n\
Population - {}\n\
Cases - {}\n\
Tests Performed - {}\n\
Recovered - {}\n\
Active Cases - {}\n\
Critical - {}\n\
Deaths - {}\n\
---------------------------------------------------------------------\n\
----- Today -----\n\
Cases- {}\n\
Recovered - {}\n\
---------------------------------------------------------------------\n\
----- Statistics per unit of population -----\n\
Cases Per Million - {}\n\
Tests Per Million - {}\n\
Active Cases Per Million - {}\n\
Recovered Per Million - {}\n\
Critical Cases Per Million - {}\n\
Deaths Per Million - {}\n\
---------------------------------------------------------------------\n\
    '.format(
        country,
        population, 
        cases, 
        tests, 
        recovered, 
        active, 
        critical, 
        deaths, 
        todayCases, 
        todayRecovered,
        casesPerOneMillion,
        testsPerOneMillion,
        activePerOneMillion,
        recoveredPerOneMillion,
        criticalPerOneMillion,
        deathsPerOneMillion
    )