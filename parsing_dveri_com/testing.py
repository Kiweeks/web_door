from urllib.parse import urlparse
from bs4 import BeautifulSoup
from os.path import join
from os import makedirs
import requests

def get_domain(link: str) -> str:
    return urlparse(link).netloc

link = 'https://dveri.com/catalog/vhodnye-dveri/porta-r/milo-bukle-chernoe-bianco-veralinga?option_id=8218'

resp = requests.get(link)
result = link + '\n\n'

bs = BeautifulSoup(resp.text, 'lxml')

title = bs.find('h1').text.strip()
title_two = bs.find('div',  class_='product__wrap').find('div', class_='product__collection').text
result += title + ' ' + title_two + '\n\n'
params = bs.find('li', class_='tabs__content-item active').find_all('div', class_="product__property")

for param in params:
    name = param.find('div', class_='product__property-name').text.strip()
    value = param.find('div', class_='product__property-value').text.strip()
    result += f"{name} {value}\n"

result += '\n'
sizes = bs.find('div', class_='product__size-wrap').find_all('div', class_='product__size-list')

for size in sizes:
    result += size.text.strip()

# print(sizes)

print(result)
# print(bs.find('div', 'product__img-wrap').find('img')['src'])
