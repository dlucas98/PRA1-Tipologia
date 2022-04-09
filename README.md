## PRA1-Tipologia
Desarrollo de la práctica 1 de la asignatura Tipología y ciclo de vida de los datos.

# Descripción de la práctica
Esta práctica comprende el scraping de la página web de [basketball-reference](https://www.basketball-reference.com/) para extraer los datos de los partidos de una temporada de la NBA, obteniendo un dataset que muestre las estadísticas de todos los jugadores que hayan participado.

# Miembros del equipo
Para el desarrollo de esta práctica se ha tabajado en equipo con los integrantes **Francisco Javier Cantero Zorita** y **David Lucas Torres**.

# Dependencias
Para poder ejecutar el código de scraping, se requieren las librerías:
```
pip install beautifulsoup4
pip install request
pip install pandas
pip install datetime
pip install argparse
```

# Ejecutar el código
Para hacer la llamada al código que consigue el dataset, se deben especificar las fechas de inicio y fin de la temporada (o cualquier fecha deseada) y el nombre del fichero de salida donde se obtendrá el dataset.

La forma de ejecutarlo será:

```
python main.py --startDate [fecha de inicio] --endDate [fecha de final] --output [fichero de salida]
```

O de forma alternativa simplificada:

```
python main.py -s [fecha de inicio] -e [fecha de final] -o[fichero de salida]
```

Es importante que el formato de la fecha sea DD-MM-YYYY.

# Resultado de la ejecución
Al ejecutar el código se obtiene un archivo *csv* con el dataset de las estadísticas de los jugadores, con los siguientes campos:

- **Nombre:** Indica el nombre del jugador al que se refiere el registro.
- **Equipo:** Especifica el equipo en el que juega el jugador para un registro.
- **MP:** *(Minutes played)* Indica los minutos que ha jugado en total un jugador.
- **FG:** *(Field goals)* Indica los tiros de campo anotados (sin contar los tiros libres)
- **FGA:** *(Field goal attempts)* Indica los intentos de anotar tiros de campo.
- **FG3:** *(3-point field goals)* Indica los tiros triples anotados por un jugador.
- **FG3A:** *(3-point field goal attempts)* Indica los intentos de tiro triple.
- **FT:** *(Free throws)* Indica los tiros libres que ha anotado un jugador.
- **FTA:** *(Free throw attempts)* Indica el total de tiros libres lanzados.
- **ORB:** *(Offensive rebounds)* Indica los rebotes ofensivos logrados por un jugador.
- **DRB:** *(Defensive rebounds)* Indica los rebotes defensivos logrados por un jugador.
- **AST:** *(Assists)* Indica las asistencias de puntos que ha realizado un jugador.
- **STL:** *(Steals)* Indica los robos de posesión del balón que ha logrado un jugador.
- **BLK:** *(Blocks)* Indica los puntos que ha conseguido evitar un jugador mediante bloqueos.
- **TOV:** *(Turnovers)* Indica las pérdidas de balón sufridas por un jugador.
- **PF:** *(Personal fouls)* Indica las faltas personales que ha provocado un jugador.
- **PTS:** *(Points)* Indica el total de puntos anotados por un jugador.
- **G:** *(Games)* Indica los juegos totales en los que ha participado un jugador
- **PER:** *(Player efficiency rating)* Resume todos los datos anteriores mediante un valor numérico.





