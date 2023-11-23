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

sides = bs.find('td', id='size_selecting').find_all('div')

for side in sides:
    # values = side.find('div', class_='list-title').text.strip()
    result += f"{side.text.strip()}\n"
result += '\n\n'

params = bs.find('table', id='opisanie_table').find_all('tr')

for param in params:
    if param.find('strong') is None and param.find('td'):
        continue
    name = param.find('strong').text.strip()
    value = param.find_all('td')[1].text.strip()
    result += f"{name}: {value}\n"

# colors = bs.find_all()

# for color in colors:
#     # pass
#     if 'title' in  color:
#         print(color)result += f'{bs.find("div", class_="_headline").text}: {bs.find("span", class_="_value").text}' + '\n\n'


# photos = bs.find_all('td', valign="top")
# files = []
# for photo in photos:
#     full_path = 'https://' + get_domain(link) + f'/{photo.find("img")["src"]}'
#     name = photo.find("img")["src"].split('/')[-1]
#     print(photo)
#     files.append({'name': name, 'data': requests.get(full_path).content})

print(result)