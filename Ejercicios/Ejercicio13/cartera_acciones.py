import pandas as pd

# Extraer información de NASDAQ-100
url_nasdaq = "https://en.wikipedia.org/wiki/NASDAQ-100"
# Crear una tabla de pandas con la información de la página
nasdaq_tables = pd.read_html(url_nasdaq)
# Seleccionar la tabla con los nombres de las acciones
nasdaq_companies = nasdaq_tables[4]
# Crear un diccionario con los nombres de las acciones y sus códigos
cartera = nasdaq_companies.set_index('Company')['Ticker'].to_dict()
# Cambiar los nombres de las keys del diccionario a minúsculas
cartera = {key.lower(): value for key, value in cartera.items()}
# Cambiar el nombre de la key de Alphabet a google
cartera['google'] = cartera.pop('alphabet inc. (class a)')
cartera.pop('alphabet inc. (class c)')