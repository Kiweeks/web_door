from urllib.parse import urlparse
from bs4 import BeautifulSoup
from os.path import join
from os import makedirs
import requests

links = (
    'https://www.альдорс.рф/product-page/лофт-зеркало-бетон-светлый',
    'https://www.альдорс.рф/product-page/лофт-зеркало-бетон-снежный',
    'https://www.альдорс.рф/product-page/кова-металл-металл',
    'https://www.альдорс.рф/product-page/кова-мини-капучино',
    'https://www.альдорс.рф/product-page/альт-зеркало-лиственница',
    'https://www.альдорс.рф/product-page/альт-зеркало-дуб-коньячный',
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