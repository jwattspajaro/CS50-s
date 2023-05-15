# Definir la función principal del programa
def main():
    names = []

    # Leer nombres hasta que el usuario ingrese EOF (Ctrl-D)
    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass

    # Crear el mensaje de despedida
    farewell = "Adiós, adiós, a "
    if len(names) == 1:
        farewell += names[0]
    elif len(names) == 2:
        farewell += f"{names[0]} y {names[1]}"
    else:
        farewell += ", ".join(names[:-1]) + f", y {names[-1]}"

    # Imprimir el mensaje de despedida
    print(farewell)

# Verificar si el archivo se está ejecutando como un programa independiente
if __name__ == "__main__":
    # Llamar a la función principal
    main()
