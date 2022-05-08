import requests
from bs4 import BeautifulSoup
import pandas as pd

# Задача - спарсить данные о сдаваемых в Москве квартирах в таблицу
# 1) Спарсить ссылки на страницы о квартирах со страницы поиска по фильтрам
# 2) Спарсить данные по ссылкам

params = {'deal_type': 'rent', 'engine_version':'2', 'is_by_homeowner':'1', 'offer_type':'flat', 'region':'1', 'room1':'1', 'room2':'1', 'room3':'1', 'room4':'1', 'room5':'1', 'room6':'1', 'room7':'1', 'room9':'1', 'type':'4'}

request = requests.get('https://www.cian.ru/cat.php', params=params)

