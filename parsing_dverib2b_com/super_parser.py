from urllib.parse import urlparse
from bs4 import BeautifulSoup
from os.path import join
from os import makedirs
import requests

links = (
    'https://dverib2b.ru/catalog/dveri_oka/massiv_olkhi_beyts/16088/',
    'https://dverib2b.ru/catalog/dveri_oka/massiv_olkhi_beyts/18303/',
    'https://dverib2b.ru/catalog/dveri_oka/massiv_olkhi_gerda_emal_beyts/31821/',
    'https://dverib2b.ru/catalog/dveri_oka/massiv_duba_emal/32230/',
    'https://dverib2b.ru/catalog/dveri_oka/massiv_sosny_strukturirovannyy_beyts/31936/',
    'https://dverib2b.ru/catalog/dveri_oka/massiv_sosny_strukturirovannyy_emal/15021/',
    'https://dverib2b.ru/catalog/dveri_oka/massiv_duba_beyts/31573/',
)

def write_result(index: int, result: str, files: list):
    makedirs(f'door-{index}', exist_ok=True)
    with open(join(f'door-{index}', 'data.txt'), 'w+', encoding= "utf-8") as file:
        file.write(result)

    for file in files:
        with open(join(f'door-{index}', file['name']), 'wb') as img:

            img.write(file['data'])


def get_domain(link: str) -> str:
    return urlparse(link).netloc


def as_doors(index: int, link: str) -> dict:
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

    write_result(index, result, files)

if __name__ == '__main__':
    for index, link in enumerate(links, start=1):
        as_doors(index, link)