from urllib.parse import urlparse
from bs4 import BeautifulSoup
from os.path import join
from os import makedirs
import requests

def get_domain(link: str) -> str:
    return urlparse(link).netloc

link = 'https://dverib2b.ru/catalog/dveri_oka/massiv_olkhi_beyts/16088/'

resp = requests.get(link)
result = link + '\n\n'

bs = BeautifulSoup(resp.text, 'lxml')

title = bs.find('div', class_='c-page-headline').find('h1').text.strip()
result += title + '\n\n'

result += f'{bs.find("div", class_="_headline").text}: {bs.find("span", class_="_value").text}' + '\n\n'

params = bs.find('div', class_='_text').text
result += params

photos = bs.find('div', class_='_slider').find_all('a')
files = []
for photo in photos:
    full_path = 'https://' + get_domain(link) + f'/{photo.find("img")["src"]}'
    name = photo.find("img")["src"].split('/')[-1]

    files.append({'name': name, 'data': requests.get(full_path).content})

print()