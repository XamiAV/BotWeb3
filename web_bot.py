import requests
from bs4 import BeautifulSoup

def buscar_en_pagina_web(nombre, apellido):
    # URL de la página web donde se realizará la búsqueda (reemplaza 'URL_DE_LA_PAGINA' con la URL real)
    url = 'https://informes.nosis.com/?utm_source=google&utm_medium=cpc&utm_campaign=googleads&utm_id=informes-nosis&utm_term=dni%20por%20nombre&gad=1&gclid=Cj0KCQjwwvilBhCFARIsADvYi7JvxH3LP-lTD5Q1kPZGKsog94C1-QqBLLPehYbDrCUGEeD6lrt2z4AaAuZqEALw_wcB'

    # Realizar la solicitud HTTP GET para obtener el contenido de la página
    response = requests.get(url)

    # Comprobar si la solicitud fue exitosa (código de estado 200 indica éxito)
    if response.status_code == 200:
        # Analizar el contenido HTML de la página web
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontrar el campo de entrada donde se ingresa el nombre y establecer el valor
        nombre_input = soup.find('input', {'class': 'bsq', 'id': 'Busqueda_Texto'})
        nombre_input['value'] = f'{nombre} {apellido}'

        # Enviar el formulario (u otra acción según el caso)
        # Para esto, puedes usar la biblioteca requests para enviar una solicitud POST con los datos actualizados
        # y obtener la respuesta con los resultados de la búsqueda.
        # Esto dependerá de cómo esté implementada la búsqueda en la página web específica.

        # Imprimir el contenido HTML de la página (solo para ver cómo se ve)
        print(soup.prettify())
    else:
        print("Error al realizar la solicitud HTTP.")

def main():
    nombre = input("Ingresa el nombre: ")
    apellido = input("Ingresa el apellido: ")
    buscar_en_pagina_web(nombre, apellido)

if __name__ == "__main__":
    main()