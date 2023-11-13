from urllib.parse import urlparse
from bs4 import BeautifulSoup
from os.path import join
from os import makedirs
import requests

links = (
    'https://verda-m.ru/catalog/metall-dveri/metallicheskie-dveri-vm/dver-met-vm-100/',
    'https://verda-m.ru/catalog/metall-dveri/metallicheskie-dveri-vm/dver-met-vm-103/',
)

def write_result(index: int, result: str):
    makedirs(f'door-{index}', exist_ok=True)
    with open(join(f'door-{index}', 'data.txt'), 'w+') as file:
        encoding = "utf-8"
        file.write(result)

    # for file in files:
    #     with open(join(f'door-{index}', file['name']), 'wb') as img:
    #         img.write(file['data'])


def get_domain(link: str) -> str:
    return urlparse(link).netloc


def as_doors(index: int, link: str) -> dict:
    resp = requests.get(link)
    result = link + '\n\n'

    bs = BeautifulSoup(resp.text, 'lxml')

    title = bs.find('h1').text.strip()
    result += title + '\n\n'
    params = bs.find('ul', class_='list-box').find_all('li')

    for param in params:
        name = param.find('div', class_='list-title').text.strip()
        value = param.find('div', class_='list-value').text.strip()
        result += f"{name} {value}\n"

    # photo = bs.find('div', class_='fancybox-placeholder')
    # files = []
    # full_path = 'https://' + get_domain(link) + f'/{photo["src"]}'
    # name = photo["src"].split('/')[-1]
    # files.append({'name': name, 'data': requests.get(full_path).content})

    write_result(index, result)

if __name__ == '__main__':
    for index, link in enumerate(links, start=1):
        as_doors(index, link)