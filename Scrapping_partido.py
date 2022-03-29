import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
#tables[8] tables[0]

partido = 'https://www.basketball-reference.com/boxscores/202110310LAL.html' 
bruto = requests.get(partido)
a = bruto.content
soup_2 = BeautifulSoup(a)
tables = soup_2.find_all("table")
jugadores = []
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
                if(cells[0].text == 'Did Not Play'):
                    datos_jugador = {
                        'Nombre': jugador,
                        'Equipo': nombre_equipo,
                        'MP': '0',
                        'FG': '0',
                        'FGA': '0',
                        'FG3': '0',
                        'FG3A': '0',
                        'FT': '0',
                        'FTA': '0',
                        'ORB': '0',
                        'DRB': '0',
                        'AST': '0',
                        'STL': '0',
                        'BLK': '0',
                        'TOV': '0',
                        'PF': '0',
                        'PTS': '0',
                        'PLUS_MINUS': '0'
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
                        'FG': fg,
                        'FGA': fga,
                        'FG3': fg3,
                        'FG3A': fg3a,
                        'FT': ft,
                        'FTA': fta,
                        'ORB': orb,
                        'DRB': drb,
                        'AST': ast,
                        'STL': stl,
                        'BLK': blk,
                        'TOV': tov,
                        'PF': pf,
                        'PTS': pts,
                        'PLUS_MINUS': plus_minus
                    }
                    jugadores.append(datos_jugador)
estadisticas = pd.DataFrame(jugadores)            
