from urllib.parse import urlparse
from bs4 import BeautifulSoup
from os.path import join
from os import makedirs
import requests

def get_domain(link: str) -> str:
    return urlparse(link).netloc

link = 'https://www.альдорс.рф/product-page/лофт-зеркало-бетон-светлый'
resp = requests.get(link)
result = link + '\n\n'

bs = BeautifulSoup(resp.text, 'lxml')

title = bs.find('h1').text.strip()
result += title + '\n\n'
params = bs.find('pre', class_='_28cEs').find_all()

for param in params:
    result += f"{param.text}\n"
#
photos = bs.find_all('div', class_='main-media-image-wrapper-hook')

for photo in photos:
    print(photo)

# files = []
# for photo in photos:
#     full_path = 'https://' + get_domain(link) + f'/{photo.find("img")["src"]}'
#     name = photo.find("img")["src"].split('/')[-1]
#
#     files.append({'name': name, 'data': requests.get(full_path).content})

# print(photos)

# print(bs.find('div', 'product__img-wrap').find('img')['src'])
