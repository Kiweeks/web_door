from urllib.parse import urlparse
from bs4 import BeautifulSoup
from os.path import join
from threading import Thread
import requests
import sqlite3
from PIL import Image
import io

links = (
    'https://vantage.su/dvernye-ruchki/575-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/82-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/304-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/86-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/83-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/202-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/204-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/711-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/205-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/478-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/572-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/573-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/295-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/419-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/420-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/576-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/207-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/4-dvernye-ruchki-na-rozetke.html',
    'https://vantage.su/dvernye-ruchki/13-dvernye-ruchki-na-rozetke.html',
    'https://vantage.su/dvernye-ruchki/24-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/28-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/29-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/33-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/35-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/38-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/210-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/214-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/215-dvernye-ruchki.htm',
    'https://vantage.su/dvernye-ruchki/219-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/91-dvernye-ruchki-alyuminievye.html',
    'https://vantage.su/dvernye-ruchki/94-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/595-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/93-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/50-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/54-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/61-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/66-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/291-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/71-dvernye-ruchki.html',
    'https://vantage.su/dvernye-ruchki/73-dvernye-ruchki.html',
)
    # 'https://disk.yandex.ru/i/Mh29dgkjQRj3WA',
    # 'https://disk.yandex.ru/i/cMFBoB-XIWPluQ',
    # 'https://disk.yandex.ru/i/dr9Shh2mBNmNbw',
    # 'https://disk.yandex.ru/i/2HBwBof9F7uUGQ',
    # 'https://disk.yandex.ru/i/eI1dWvSVBVnyoA',
    # 'https://disk.yandex.ru/i/Ln32D9XaTKS_3A',
    # 'https://disk.yandex.ru/i/JMmdF7t-qO4F8A',
    # 'https://disk.yandex.ru/i/gxISN77cPWhhBQ',
    # 'https://disk.yandex.ru/i/UUU1e6ucOg33jw',
    # 'https://disk.yandex.ru/i/De-dHgXlfsN3Vw',
    # 'https://disk.yandex.ru/i/8Y_K71W4KDAfwA',
    # 'https://disk.yandex.ru/i/dCti6Z4MfXZP_A',
    # 'https://disk.yandex.ru/i/p6cmReATjDRXMg',
    # 'https://disk.yandex.ru/i/7Bt-5uR05oEhqg',
    # 'https://disk.yandex.ru/i/_7k06PTTtSOTTA',
    # 'https://disk.yandex.ru/i/u4fZp7dxFmLTNA',
    # 'https://disk.yandex.ru/i/ZVaBgbBriIQNZA',
    # 'https://disk.yandex.ru/i/WQ7JqhCipTPdUg',
    # 'https://disk.yandex.ru/i/II_8CCr3JBVu8A',
    # 'https://disk.yandex.ru/i/XF4DC-NmvbfToA',
    # 'https://disk.yandex.ru/i/EcOOy-lqP9EzfQ',
    # 'https://disk.yandex.ru/i/elB_t8qVJ6gWKw',
    # 'https://disk.yandex.ru/i/k84m8zbgstdjwg',
    # 'https://disk.yandex.ru/i/oecTlzUX4-SJkg',
    # 'https://disk.yandex.ru/i/Y2KaSH-87daqKg',
    # 'https://disk.yandex.ru/i/48H25Y77056nvw',
    # 'https://disk.yandex.ru/i/AnK-gjlXqxE9Fg',
    # 'https://disk.yandex.ru/i/AlPbMQ_KRiDshQ',
    # 'https://disk.yandex.ru/i/SOxW_8_pntAMxQ',
    # 'https://disk.yandex.ru/i/Pk4r392fuaQ1cA',
    # 'https://disk.yandex.ru/i/zeoHseBfxxXmhA',
    # 'https://disk.yandex.ru/i/TJa4tTiIhGdCNQ',
    # 'https://disk.yandex.ru/i/-QWj6AENAGHHLg',
    # 'https://disk.yandex.ru/i/TDxid6CtfvXkFA',
    # 'https://disk.yandex.ru/i/Z4GifBtJGUiJhw',
    # 'https://disk.yandex.ru/i/e10L5KuK3Lcp7A',
    # 'https://disk.yandex.ru/i/LRDg972XG6EaBQ',
    # 'https://disk.yandex.ru/i/aJGlRLPqfYu3rQ',
    # 'https://disk.yandex.ru/i/0lbMOnJziSA4cA',
    # 'https://disk.yandex.ru/i/UFf1H77F7xvK9w',
    # 'https://disk.yandex.ru/i/pdIBkH8bVpCRsQ',
    # 'https://disk.yandex.ru/i/x0SBoM7MgbD30A',
    # 'https://disk.yandex.ru/i/y0G8UxfNVScBzw',
    # 'https://disk.yandex.ru/i/SJ7rFOO037XnHA',
    # 'https://disk.yandex.ru/i/gubQlPL9N47ONQ',
    # 'https://disk.yandex.ru/i/2dW0LEEG0MnQUg',
    # 'https://disk.yandex.ru/i/YhYTZL8rreJyag',
    # 'https://disk.yandex.ru/i/EpkkKtpFOgHYdg',
    # 'https://disk.yandex.ru/i/CHh2tq3Vzbg3Wg',
    # 'https://disk.yandex.ru/i/VA1Wc3k2S1IRig',
    # 'https://disk.yandex.ru/i/mAtwxykNsjr0jQ',
    # 'https://disk.yandex.ru/i/nvaAUgtNdTRzrQ',
    # 'https://disk.yandex.ru/i/XjsaeUZVhqyBmg',
    # 'https://disk.yandex.ru/i/bTlLEkZmUhR9oQ',
    # 'https://disk.yandex.ru/i/ID2SIkULFFeiKA',
    # 'https://disk.yandex.ru/i/W0Ex2uWHWIGN-Q',
    # 'https://disk.yandex.ru/i/N3VfjOOEN-DB0A',
    # 'https://disk.yandex.ru/i/EOlewBDiJ00oNQ',
    # 'https://disk.yandex.ru/i/tiBTGtqntqLsKg',
    # 'https://disk.yandex.ru/i/dFWJ89M16OTdQA',
    # 'https://disk.yandex.ru/i/GoVzCszweIpCRA',
    # 'https://disk.yandex.ru/i/Y0o4OoSLAe_CbA',
    # 'https://disk.yandex.ru/i/i7HSCWkJfJg-uQ',
    # 'https://disk.yandex.ru/i/AGZqMbGl3IKAKg',
    # 'https://disk.yandex.ru/i/J-rvaO8Pbp_JvA',
    # 'https://disk.yandex.ru/i/mNEbws5JGmlGHA',
    # 'https://disk.yandex.ru/i/srSo3L-X--6DUw',
    # 'https://disk.yandex.ru/i/erWNr21Q-Sl_pQ',
    # 'https://disk.yandex.ru/i/MAzOnsYAJeEJ5Q',
    # 'https://disk.yandex.ru/i/upHfMxj-oNXHiA',


def write_result(files: list):
    for file in files:
        with open(join(f'photo_door', file['name']), 'wb') as img:
            img.write(file['data'])


def get_domain(link: str) -> str:
    return urlparse(link).netloc


def as_doors(index: int, link: str) -> dict:
    resp = requests.get(link)
    print(index, link)
    bs = BeautifulSoup(resp.text, 'lxml')

    img = bs.find('img', id='main_image_big')['src']
    full_path = 'https://' + get_domain(link) + f'/{img}'
    name = img.split('/')[-1]

    img_color = tuple(filter(lambda obj: obj['src'].startswith('/xml/colors_images'), bs.find_all('img')))[0]

    COLOR = {
        'code': get_img_color(requests.get(f'https://dver.com/{img_color["src"]}').content),
        'color': img_color['title']
    }

    TITLE = ' '.join(bs.find('h1').text.replace(COLOR['color'], '').split()[:-5])
    BRAND = 'ТЕКОНА'

    CATEGORY_ID = 4
    DOOR_TYPE = 7 if 'стекло' not in TITLE else 8

    SIZES = get_sizes(bs)
    PARAMS = get_params(bs)
    DESCRIPTION = "Наши межкомнатные двери — идеальное сочетание стиля и функциональности. Улучшите интерьер вашего дома, выбрав из нашего разнообразного ассортимента. Инновационные материалы и заботливо продуманный дизайн обеспечивают не только визуальное восхищение, но и долговечность использования. Откройте для себя комфорт и элегантность с нашими межкомнатными дверями, которые подчеркнут уникальность каждого помещения."
    insert_in_db(TITLE, BRAND, CATEGORY_ID, DOOR_TYPE, PARAMS, DESCRIPTION, COLOR, SIZES,
                 {'name': name, 'data': requests.get(full_path).content})


def insert_in_db(title, brand, category_id, type_id, params, description, color, sizes, img):
    write_result(files=[img])
    db_path = r'C:\Users\Hiro\Documents\GitHub\web_door\kiweeks\db.sqlite3'
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    id = cur.execute('INSERT INTO main_door (title, brand, properties, type_id, category_id, description)'
                     'VALUES (?,?,?,?,?,?);', (title, brand, params, type_id, category_id, description)).lastrowid

    cur.execute('INSERT INTO main_photo_door (doors_id, photos) VALUES (?, ?)', (id, 'photo_door/'+img['name']))
    color_id = cur.execute("SELECT id FROM main_color_inside WHERE code = ?", (color['code'],)).fetchone()
    print(color_id)
    if color_id is None:
        color_id = cur.execute("INSERT INTO main_color_inside (color, code) VALUES (?, ?)", (color['color'],color['code'])).lastrowid
    else:
        color_id = color_id[0]

    cur.execute("INSERT INTO main_door_colors_inside (door_id, color_inside_id) VALUES (?, ?)",(id, color_id))
    cur.execute("INSERT INTO main_door_sides (door_id, side_of_door_id) VALUES (?, 1), (?, 2)",(id, id))
    for size in sizes:
        size_id = cur.execute("SELECT id FROM main_size_door WHERE sizes_doors = ?", (size,)).fetchone()
        if size_id is None:
            size_id = cur.execute("INSERT INTO main_size_door (sizes_doors ) VALUES (?)", (size, )).lastrowid
        else:
            size_id = size_id[0]

        cur.execute("INSERT INTO main_door_sizes (door_id, size_door_id) VALUES (?,?)", (id, size_id))
    con.commit()
    cur.close()


if __name__ == '__main__':
    a = 0
    q = []
    for index, link in enumerate(links, start=1):
        as_doors(index, link)
