import requests
import json
from config import API_LINK

def get_response_global(param):
    response = requests.get(API_LINK+param).json()

    return response


# In this case, param is the parameter that countries will be sorted by
def top(how_much, param):
    response = requests.get(API_LINK+'countries?sort='+param).json()

    for i in range(how_much):
        message = response[i]
        country = message['country']
        parameter = message[param]
        print(str(i + 1) + ": " + country + ' - ' + str(parameter) + " " + param)


def my_country(country):
    response = requests.get(API_LINK+'countries/'+country).json()
    return response

