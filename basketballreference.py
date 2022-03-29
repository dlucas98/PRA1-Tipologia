import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.basketball-reference.com/leagues/NBA_2022_games-october.html'
page = requests.get(url)
soup = BeautifulSoup(page.text)

games = []
tds = soup.find_all("td")

for td in tds:
    a = td.next_element
    if a.name == 'a':
        href = a['href'] 
        if (href.find("/boxscores") != -1):
            #print(href) #Para ver los partidos que se han cogido
            games.append(href)
jugadores = []     
for i in range(len(games)):            
    partido = 'https://www.basketball-reference.com' + games[i]
    bruto = requests.get(partido)
    a = bruto.content
    soup_2 = BeautifulSoup(a)
    tables = soup_2.find_all("table")
    #tables[0].find('caption').text
    for table in tables:
        titulo = table.find('caption').text 
        if('Basic' in titulo): #Nos quedamos con las estadísticas basicas
            table_body = table.find('tbody')
            nombre_equipo=titulo.split(' Basic')[0]
            for row in table_body.findAll('tr'):
                nombre = row.find('a')      
                if (nombre is not None):
                    jugador=nombre.text
                    cells = row.findAll('td')
                    if(cells[0].text == 'Did Not Play' or cells[0].text == 'Did Not Dress'):
                        datos_jugador = {
                            'Nombre': jugador,
                            'Equipo': nombre_equipo,
                            'MP': '0',
                            'FG': 0,
                            'FGA': 0,
                            'FG3': 0,
                            'FG3A': 0,
                            'FT': 0,
                            'FTA': 0,
                            'ORB': 0,
                            'DRB': 0,
                            'AST': 0,
                            'STL': 0,
                            'BLK': 0,
                            'TOV': 0,
                            'PF': 0,
                            'PTS': 0
                        }   
                        jugadores.append(datos_jugador) 
                    else:    
                        mp = cells[0].text
                        fg = cells[1].text
                        fga = cells[2].text
                        fg3 = cells[4].text
                        fg3a = cells[5].text
                        ft = cells[7].text
                        fta = cells[8].text
                        orb = cells[10].text
                        drb = cells[11].text
                        ast = cells[13].text
                        stl = cells[14].text
                        blk = cells[15].text
                        tov = cells[16].text
                        pf = cells[17].text
                        pts = cells[18].text
                        plus_minus = cells[19].text
                        datos_jugador = {
                            'Nombre': jugador,
                            'Equipo': nombre_equipo,
                            'MP': mp,
                            'FG': int(fg),
                            'FGA': int(fga),
                            'FG3': int(fg3),
                            'FG3A': int(fg3a),
                            'FT': int(ft),
                            'FTA': int(fta),
                            'ORB': int(orb),
                            'DRB': int(drb),
                            'AST': int(ast),
                            'STL': int(stl),
                            'BLK': int(blk),
                            'TOV': int(tov),
                            'PF': int(pf),
                            'PTS': int(pts)
                        }
                        jugadores.append(datos_jugador)

estadisticas = pd.DataFrame(jugadores)            

for i in range(len(estadisticas)):
    if(len(estadisticas.iloc[i,2].split(':'))==2):
        (m, s) = estadisticas.iloc[i,2].split(':')
        result = int(m) + int(s)/60
        estadisticas.iloc[i,2]=round(result)
