# El código importa el módulo re para trabajar con expresiones regulares.
# La función main solicita al usuario que ingrese un código HTML y luego llama a la función parse con el código HTML ingresado como argumento. 
# Luego se imprime el resultado de la función parse.
# La función parse recibe una cadena de texto que representa un código HTML. 
# Utiliza una expresión regular para buscar la URL de un video de YouTube en el atributo src de un elemento iframe. 
# La expresión regular está diseñada para capturar el ID del video. Si se encuentra una coincidencia, 
# se construye la URL corta de 'youtu.be' con el ID del video y se devuelve. Si no se encuentra ninguna coincidencia, se devuelve None.
# La condición if __name__ == "__main__": 
#se utiliza para ejecutar la función main si el archivo se está ejecutando directamente y no siendo importado como un módulo.

import re  # Importamos el módulo 're' para trabajar con expresiones regulares

def main():
    # Solicitamos al usuario que ingrese el código HTML y llamamos a la función 'parse'
    print(parse(input("HTML: ")))

def parse(s):
    # Definimos una expresión regular para buscar la URL de YouTube en el atributo 'src' de un elemento 'iframe'
    regex = r'<iframe.*?src="(?:https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)|http://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+))".*?></iframe>'

    # Realizamos la búsqueda utilizando la expresión regular
    match = re.search(regex, s)

    # Si se encuentra una coincidencia, se retorna la URL corta de 'youtu.be'
    if match:
        video_id = match.group(1) if match.group(1) else match.group(2)
        return f'https://youtu.be/{video_id}'
    else:
        return None  # Si no se encuentra ninguna coincidencia, se retorna None

if __name__ == "__main__":
    main()
