import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.nba.com/games'
page = requests.get(url)

contenido = page.content

soup = BeautifulSoup(contenido)


lis = soup.find_all("li")

games = []

for li in lis:
    a = li.next_element
    #(a) Esto es una comparación que he probado, lo puedes borrars
    if a.name == 'a':
        href = a['href']
        if href[0] == '/':
            if (href.find("box-score#box-score") != -1):
                games.append(href)
            

for i in range(0,1):#Está a 1 porque solo he probado con el primer valor
    partido = 'https://www.nba.com' + str(games[i])
    print(partido)
    bruto = requests.get(partido)
    a = bruto.content
    soap_2 = BeautifulSoup(a)
    texto = str(soap_2.find_all("script"))
    with open("contentasa.txt", "w") as f:
    # f.write(str(soup.prettify()))
        f.write(texto)
    print(texto.split(sep='}'))
