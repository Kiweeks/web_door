from urllib.parse import urlparse
from bs4 import BeautifulSoup
from os.path import join
from os import makedirs
import requests

links = (
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_shponirovannye_tekona_freim_03_gluhoe_dub_art-F0000051115',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_shponirovannye_tekona_strato_02_so_steklom_tonirovannyi_chernyi_dub_art-F0000050536',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_01_gluhoe_molochnyi_ral_9010_art-F0000059246',
    'https://dver.com/mezhkomnatnye-dveri/all/dveri_krashenye__emal__tekona_smalta_02_so_steklom_belyi_ral_9003_art-F0000057650',
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