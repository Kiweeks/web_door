from urllib.parse import urlparse
from bs4 import BeautifulSoup
from os.path import join
from os import makedirs
import requests

def get_domain(link: str) -> str:
    return urlparse(link).netloc

link = 'https://verda-m.ru/catalog/metall-dveri/metallicheskie-dveri-rossiya/dver-met-yoshkar/'

resp = requests.get(link)
result = link + '\n\n'

bs = BeautifulSoup(resp.text, 'lxml')

# title = bs.find('h1').text.strip()
# result += title + '\n\n'
# params = bs.find('ul', class_='list-box').find_all('li')
#
# for param in params:
#     name = param.find('div', class_='list-title').text.strip()
#     value = param.find('div', class_='list-value').text.strip()
#     result += f"{name} {value}\n

photo = bs.find('div', class_='fancybox-placeholder').find('img')
# files = []
# full_path = 'https://' + get_domain(link) + f'/{photo["src"]}'
# name = photo["src"].split('/')[-1]
# files.append({'name': name, 'data': requests.get(full_path).content})

print(photo)
# print(bs.find('div', 'product__img-wrap').find('img')['src'])
