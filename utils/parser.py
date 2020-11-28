import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://www.who.int/emergencies/diseases/novel-coronavirus-2019/media-resources/news")
html = BS(r.content, 'html.parser')

def parse():
    i = 0
    output = {}

    for el in html.select('.list-view'):
        title = el.select('.heading')
        date = el.select('.sub-title')
        
        output.update({title[0].text :date[0].text})

        i+=1
        if i == 5:
            break

    text = ['Latest new about COVID-19: ', '']

    for t, d in output.items():
        text.append('-----')
        text.append(t + '\n' + d)

    text = '\n'.join(text)
    return text        