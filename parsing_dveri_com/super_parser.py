from urllib.parse import urlparse
from bs4 import BeautifulSoup
from os.path import join
from os import makedirs
import requests

links = (
    'https://dveri.com/catalog/vhodnye-dveri/porta-r/milo-bukle-chernoe-bianco-veralinga?option_id=8218',
    # 'https://dveri.com/catalog/vhodnye-dveri/porta-r/milo-bukle-chernoe-cappuccino-veralinga?option_id=8210',
    # 'https://dveri.com/catalog/vhodnye-dveri/porta-r/milo-bukle-chernoe-wenge-veralinga?option_id=8214',
    # 'https://dveri.com/catalog/vhodnye-dveri/porta-r/lajn-bukle-chernoe-snow-melinga?option_id=9507',
    # 'https://dveri.com/catalog/vhodnye-dveri/porta-r/lajn-bukle-chernoe-snow-art?option_id=12457',
    # 'https://dveri.com/catalog/vhodnye-dveri/porta-r/lajn-bukle-chernoe-look-art?option_id=9507',
    # 'https://dveri.com/catalog/vhodnye-dveri/porta-r/lajn-bukle-chernoe-cappuccino-veralinga?option_id=9515',
    # 'https://dveri.com/catalog/vhodnye-dveri/porta-r/lajn-bukle-chernoe-slate-art?option_id=9527',
    # 'https://dveri.com/catalog/vhodnye-dveri/porta-r/lajn-bukle-chernoe-grey-melinga?option_id=9511',
    # 'https://dveri.com/catalog/vhodnye-dveri/porta-r/lajn-bukle-chernoe-wenge-veralinga?option_id=10660',
    # 'https://dveri.com/catalog/vhodnye-dveri/porta-r/graffiti-1-insajd-bukle-chernoe-snow-art',
    # 'https://dveri.com/catalog/vhodnye-dveri/porta-r/graffiti-1-insajd-bukle-chernoe-look-art?option_id=9478',
    # 'https://dveri.com/catalog/vhodnye-dveri/porta-r/graffiti-1-insajd-bukle-chernoe-slate-art?option_id=9474',
    # 'https://dveri.com/catalog/vhodnye-dveri/porta-r/prof-bukle-chernoe-bianco-veralinga?option_id=9221',
    # 'https://dveri.com/catalog/vhodnye-dveri/porta-r/prof-bukle-chernoe-cappuccino-veralinga?option_id=9221',
    # 'https://dveri.com/catalog/vhodnye-dveri/porta-r/prof-bukle-chernoe-wenge-veralinga?option_id=9225',
    # 'https://dveri.com/catalog/vhodnye-dveri/porta-r/syut-kale-bukle-chernoe-white-wood',
    # 'https://dveri.com/catalog/vhodnye-dveri/porta-r/graffiti-5-5-kale-slate-art-look-art',
    # 'https://dveri.com/catalog/vhodnye-dveri/porta-r/kyub-rbe-slate-art-snow-art',
    # 'https://dveri.com/catalog/vhodnye-dveri/porta-r/kyub-rbe-total-black-super-white',
    # 'https://dveri.com/catalog/vhodnye-dveri/porta-r/graffiti-32-32-total-black-super-white',
    # 'https://dveri.com/catalog/vhodnye-dveri/porta-r/dzhet-3-rbe-total-black-snow-melinga',
    # 'https://dveri.com/catalog/vhodnye-dveri/bravo-t/thermo-tehno-dekor-2-bukle-chernoe-cappuccino-veralinga', # c терморазрывом
)

def write_result(index: int, result: str, files: list):
    makedirs(f'door-{index}', exist_ok=True)
    with open(join(f'door-{index}', 'data.txt'), 'w+') as file:
        encoding = "utf-8"
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

    title = bs.find('h1').text.strip()
    title_two = bs.find('div', class_='product__wrap').find('div', class_='product__collection').text
    result += title + ' ' + title_two + '\n\n'
    params = bs.find('li', class_='tabs__content-item active').find_all('div', class_="product__property")

    for param in params:
        name = param.find('div', class_='product__property-name').text.strip()
        value = param.find('div', class_='product__property-value').text.strip()
        result += f"{name} {value}\n"

    photos = bs.find('div', class_='product__img product__img--double').find_all('div')
    files = []
    for photo in photos:
        full_path = 'https://' + get_domain(link) + f'/{photo.find("img")["src"]}'
        name = photo.find("img")["src"].split('/')[-1]

        files.append({'name': name, 'data': requests.get(full_path).content})

    write_result(index, result, files)

if __name__ == '__main__':
    for index, link in enumerate(links, start=1):
        as_doors(index, link)