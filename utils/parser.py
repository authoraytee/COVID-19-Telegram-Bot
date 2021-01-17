import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://covid-stat.com/")
html = BS(r.content, 'html.parser')

def parse():
    i = 0
    output = []

    for el in html.select('.news'):
        body = el.select('.new')

        output.append(body)

        
    print(output)

    text = ['Latest news about COVID-19: ', '']

    text.append(body)
    for t in output:
    #    text.append('-'*30)
        text.append(t + '\n')

    #print(text)

    text = '\n'.join(text)

    return text        