from urllib.parse import urlparse
from bs4 import BeautifulSoup
from os.path import join
from os import makedirs
import requests

def get_domain(link: str) -> str:
    return urlparse(link).netloc

link = 'https://dver.com/mezhkomnatnye-dveri/all/dveri_shponirovannye_tekona_freim_03_gluhoe_dub_art-F0000051115'

resp = requests.get(link)
result = link + '\n\n'

bs = BeautifulSoup(resp.text, 'lxml')

title = bs.find('h1').text.strip()
result += title + '\n\n'

# result += f'{bs.find("div", class_="_headline").text}: {bs.find("span", class_="_value").text}' + '\n\n'
#
sides = bs.find('td', id='size_selecting').find_all('div')

for side in sides:
    # values = side.find('div', class_='list-title').text.strip()
    result += f"{side.text.strip()}\n"
result += '\n\n'

params = bs.find('table', id='opisanie_table').find_all('tr')

for param in params:
    # name = param.find('div', class_='list-title').text.strip()
    # value = param.find('div', class_='list-value').text.strip()
    # result += f"{name} {value}\n"
    print(param.text)

# photos = bs.find('div', class_='_slider').find_all('a')
# files = []
# for photo in photos:
#     full_path = 'https://' + get_domain(link) + f'/{photo.find("img")["src"]}'
#     name = photo.find("img")["src"].split('/')[-1]
#
#     files.append({'name': name, 'data': requests.get(full_path).content})

print(params)