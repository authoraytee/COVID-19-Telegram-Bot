from aiogram import types
from utils.api_connector import get_response_global

from loader import dp, storage, bot


@dp.message_handler(commands='detailed_info')
@dp.callback_query_handler(text='detailed_info')
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):

    stat = get_response_global('all')
    population = stat['population']
    affectedCountries = stat['affectedCountries']
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

    await bot.send_message(query.from_user.id, 
    'COVID-19 Detailed Global Stats:\n\
---------------------------------------------------------------------\n\
* Statistics Are Updated Every 10 Minutes *\n\
---------------------------------------------------------------------\n\
----- Main information -----\n\
Earth\'s Population - {}\n\
Infected Countries - {}\n\
Total Cases - {}\n\
Tests Performed - {}\n\
Recovered - {}\n\
Active Cases - {}\n\
Critical - {}\n\
Deaths - {}\n\
---------------------------------------------------------------------\n\
----- Today -----\n\
Cases - {}\n\
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
    population, 
    affectedCountries, 
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
    ))
