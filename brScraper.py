import datetime
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

class brScraper():

    def __init__(self, startDate, endDate, output):
        self.url = 'https://www.basketball-reference.com'
        self.games = []
        self.players = []
        self.startDate = startDate
        self.endDate = endDate
        self.output=output
        
        
    def __buscar_partidos(self, date):
        games = []
        url = 'https://www.basketball-reference.com/boxscores/index.fcgi?month='+ str(date.month) +'&day='+ str(date.day) +'&year='+ str(date.year)
        page = requests.get(url)
        soup = BeautifulSoup(page.text)
        tds = soup.find_all("td")
        for td in tds:
            a = td.next_element.next_element
            if a.name == 'a':
                href = a['href'] 
                if (href.find("/boxscores") != -1):
                    #print(href) #Para ver los partidos que se han cogido
                    games.append(href)
                    # return href
        return(games)
    
    def __obtener_estadisticas(self,game):
        jugadores = []               
        partido = 'https://www.basketball-reference.com' + game
        bruto = requests.get(partido)
        todo = bruto.content
        soup = BeautifulSoup(todo)
        tables = soup.find_all("table")

        for table in tables:
            titulo = table.find('caption').text 
            if('Basic' in titulo): # Nos quedamos con las estadísticas basicas
                table_body = table.find('tbody')
                nombre_equipo=titulo.split(' Basic')[0]
                for row in table_body.findAll('tr'):
                    nombre = row.find('a')      
                    if (nombre is not None):
                        jugador=nombre.text
                        cells = row.findAll('td')
                        if (cells[0].text != 'Did Not Play' and cells[0].text != 'Did Not Dress' and cells[0].text != 'Not With Team'):
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

        return jugadores
      
    def __convertir_minutos(self,df):
        for i in range(len(df)):
            if(len(df.iloc[i,2].split(':'))==2):
                (m, s) = df.iloc[i,2].split(':')
                result = int(m) + int(s)/60
                df.iloc[i,2]=round(result)
            else:
                df.iloc[i,2]=int(df.iloc[i,2])

        return df

    def __calculadora_per(self, df1):
        pers = []
        for i in range(len(df1)):
            if (df1.iloc[i,2]!=0):
                per =  (df1.iloc[i,3] * 85.910 + df1.iloc[i,12] * 53.897 + df1.iloc[i,5] * 51.757 + df1.iloc[i,7] *46.845 + df1.iloc[i,13] * 39.190 
                    + df1.iloc[i,9] * 39.190 + df1.iloc[i,11] * 34.677 + df1.iloc[i,10] * 14.707 
                    - df1.iloc[i,15] * 17.174 - (df1.iloc[i,8] - df1.iloc[i,7]) * 20.091 - (df1.iloc[i,4] - df1.iloc[i,3]) * 39.190 - df1.iloc[i,14] * 53.897 ) * (1/df1.iloc[i,2]) 
                pers.append(round(per,2))
            else:
                pers.append(0)
        df2 = pd.DataFrame(pers,columns = ['PER'])
        return pd.concat([df1, df2], axis=1,)
    
    def __exportar_csv(self,df1):
        df1.to_csv(self.output+'.csv', index=None, mode='a')
    
    def scrape(self):
        print ('Scraping de las estadísticas de los jugadores de la NBA en la página' + self.url + ' entre el día: ' + str(self.startDate) + ' - ' + str(self.endDate))
        
        date = self.startDate

        while date <= self.endDate:
            self.games.append(self.__buscar_partidos(date))
            date = date + datetime.timedelta(days=1)
        
        # Acoplar lista de listas a una sola lista
        self.games = [item for sublist in self.games for item in sublist]

        for i in range(len(self.games)):
            self.players.append(self.__obtener_estadisticas(self.games[i]))

        # Acoplar lista de listas a una sola lista
        self.players = [item for sublist in self.players for item in sublist]

        # Convertir lista de players a dataframe
        df = pd.DataFrame(self.players)

        df = self.__convertir_minutos(df)

        # Convertimos la columna de minutos a entero
        df['MP'] = df['MP'].astype(int)

        # Agrupamos los datos por por el nombre y el equipo del jugador
        df1 = df.groupby(['Nombre','Equipo']).sum().reset_index()

        # Agrupamos los datos por por el nombre y el equipo del jugador y calculamos el número de veces que se agruparon
        df2 = df.groupby(['Nombre','Equipo']).size().reset_index(name='G')

        # Añadimos a df1 la columna de counts de df2
        dfout = pd.merge(df1, df2, on=['Nombre','Equipo'], how='outer')

        # Calculamos el PER
        dfout = self.__calculadora_per(dfout)

        print(str(dfout))
        self.__exportar_csv(dfout)

