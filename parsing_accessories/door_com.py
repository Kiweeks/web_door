from urllib.parse import urlparse
from bs4 import BeautifulSoup
from os.path import join
from threading import Thread
import requests
import sqlite3
from PIL import Image
import io

links = (
    'https://disk.yandex.ru/i/GoVzCszweIpCRA',
    'https://disk.yandex.ru/i/Y0o4OoSLAe_CbA',
    'https://disk.yandex.ru/i/i7HSCWkJfJg-uQ',
    'https://disk.yandex.ru/i/AGZqMbGl3IKAKg',
    'https://disk.yandex.ru/i/J-rvaO8Pbp_JvA',
    'https://disk.yandex.ru/i/mNEbws5JGmlGHA',
    'https://disk.yandex.ru/i/srSo3L-X--6DUw',
    'https://disk.yandex.ru/i/erWNr21Q-Sl_pQ',
    'https://disk.yandex.ru/i/MAzOnsYAJeEJ5Q',
    'https://disk.yandex.ru/i/upHfMxj-oNXHiA',
)



def write_result(files: list):
    for file in files:
        with open(join(f'photo_accessories', file['name']), 'wb') as img:
            img.write(file['data'])


def get_domain(link: str) -> str:
    return urlparse(link).netloc


def as_doors(index: int, link: str) -> dict:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 YaBrowser/23.11.0.0 Safari/537.36'
    }
    resp = requests.get(link, headers=headers)
    print(index, link)
    bs = BeautifulSoup(resp.text, 'lxml')

    img = bs.find('img', class_='content__image-preview')['src']
    full_path = f'https://disk.yandex.ru{img}'
    name = img.split('/')[-1]

    insert_in_db({'name': name, 'data': requests.get(full_path).content})


def insert_in_db(img):
    write_result(files=[img])
    db_path = r'C:\Users\Hiro\Documents\GitHub\web_door\kiweeks\db.sqlite3'
    con = sqlite3.connect(db_path)
    cur = con.cursor()


    cur.execute('INSERT INTO main_photo_accessories (photo) VALUES (?)', ('photo_accessories/'+img['name'],))
    con.commit()
    cur.close()


if __name__ == '__main__':
    a = 0
    q = []
    for index, link in enumerate(links, start=1):
        as_doors(index, link)
