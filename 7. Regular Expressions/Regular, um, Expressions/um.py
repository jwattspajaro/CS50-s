import re  # Importamos el módulo 're' para trabajar con expresiones regulares

def main():
    # Solicitamos al usuario que ingrese el texto para contar las ocurrencias de "um"
    print(count(input("Text: ")))

def count(s):
    # Definimos una expresión regular para contar las ocurrencias de "um" como palabra independiente (insensible a mayúsculas/minúsculas)
    regex = r'\b[Uu][Mm]\b'

    # Contamos las coincidencias utilizando 'findall' y retornamos la cantidad encontrada
    return len(re.findall(regex, s))

if __name__ == "__main__":
    main()
