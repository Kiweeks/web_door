import requests
from bs4 import BeautifulSoup
from write_file import write_data_file

link = 'https://as-doors.ru/onstock/dvustvorchataya-new.html'

response = requests.get(link)

soup = BeautifulSoup(response.text, "lxml")

name_door = soup.find("div", class_='title').text

specifications = soup.find("div", class_='table js-characteristics-block').find_all("p")

text_door = soup.find_all("div", class_='txt')[1].find("p").text

write_data_file(link, name_door, specifications, text_door)