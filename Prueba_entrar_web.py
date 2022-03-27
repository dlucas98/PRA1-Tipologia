import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.nba.com/games'
page = requests.get(url)

contenido = page.content

soup = BeautifulSoup(contenido)

with open("content.txt", "w") as f:
    f.write(str(soup.prettify()))