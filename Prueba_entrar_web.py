import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.nba.com/games'
page = requests.get(url)

contenido = page.content

soup = BeautifulSoup(contenido)

with open("content.txt", "w") as f:
    # f.write(str(soup.prettify()))
    f.write(str(soup.find_all("a")))

lis = soup.find_all("li")

games = []

for li in lis:
    a = li.next_element
    if a.name == 'a':
        href = a['href']
        if href[0] == '/':
            if (href.find("box-score#box-score") != -1):
                games.append(href)
            
print(len(games))




# print(lis.find("href"))
# soup.find(data-id="nba:games:main:box-score:cta")