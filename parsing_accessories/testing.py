from urllib.parse import urlparse
from bs4 import BeautifulSoup
from os.path import join
from os import makedirs
import requests

def as_doors(link: str) -> dict:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 YaBrowser/23.11.0.0 Safari/537.36'
    }
    resp = requests.get(link, headers=headers)
    print(link)
    bs = BeautifulSoup(resp.text, 'lxml')

    img = bs.find('img', class_='content__image-preview')
    full_path = f'https://disk.yandex.ru{img}'
    print(img)
    print(full_path)

as_doors('https://disk.yandex.ru/i/upHfMxj-oNXHiA')