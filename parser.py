import requests
from bs4 import BeautifulSoup
import pandas as pd

# Задача - спарсить данные о сдаваемых в Москве квартирах в таблицу
# 1) Спарсить ссылки на страницы о квартирах со страницы поиска по фильтрам
# 2) Спарсить данные по ссылкам
