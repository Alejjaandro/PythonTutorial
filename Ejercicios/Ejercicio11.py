import bs4
import requests

# URL de la página web
URL_BASE = 'https://books.toscrape.com/catalogue/page-{}.html'

libros_con_alto_rating = []

# Iteramos sobre las 50 páginas
for pagina in range(1, 51):
    
    URL_PAGINA = URL_BASE.format(pagina)
    resultado = requests.get(URL_PAGINA)
    # Creamos un objeto BeautifulSoup
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
    # Extraemos el contenedor de los libros
    libros = sopa.select('.product_pod')
    # Iteramos sobre cada contenedor
    for libro in libros:
        # Si el libro tiene 4 o 5 estrellas, lo añadimos a la lista
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            
            titulo = libro.select('h3 a')[0]['title']
            libros_con_alto_rating.append(titulo)
            

print(libros_con_alto_rating)