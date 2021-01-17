import requests
import json
from config import API_LINK

def get_response_global(param):
    response = requests.get(API_LINK+param).json()

    return response


# In this case, param is the parameter that countries will be sorted by
def top(how_much, param):
    response = requests.get(API_LINK+'countries?sort='+param).json()

    total_cases = []

    for i in range(how_much):
        message = response[i]
        country = message['country']
        parameter = message[param]
        get_country = str(i + 1) + ": " + country + ' - ' + str(parameter) + " " + param
        total_cases.append(get_country)

    return total_cases


def my_country(country):
    response = requests.get(API_LINK+'countries/'+country).json()
    return response

