import json
import os

# Función para validar la entrada del usuario en función de las opciones disponibles
def obtener_opcion_valida(opciones):
    while True:
        try:
            opcion = int(input())
            if opcion in opciones:
                return opcion
            else:
                raise ValueError
        except ValueError:
            print("Opción no válida, por favor ingrese un número válido.")

# Función que muestra el menú principal
def menu_principal():
    print("Menú principal:")
    print("1. Agregar alimento")
    print("2. Eliminar alimento")
    print("3. Ver lista de alimentos")
    print("4. Ver gastos en alimentos")
    print("5. Actualizar información de alimentos")
    print("6. Salir")
    while True:
        opcion = input("Seleccione una opción: ")
        if opcion in ['1', '2', '3', '4', '5', '6']:
            return int(opcion)
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


# Función principal que ejecuta el programa
def main():

    alimentos = {}
    alimentos_gastados = []

    while True:
        opcion = menu_principal()
        if opcion == 1:
            alimento_agregado = agregar_alimento()
            alimentos.update(alimento_agregado)
        elif opcion == 2:
            eliminar_alimento(alimentos)
        elif opcion == 3:
            ver_lista_alimentos(alimentos)
        elif opcion == 4:
            ver_gastos_alimentos()
        elif opcion == 5:
            modificar_alimento(alimentos)
        elif opcion == 6:
            break

# Función para agregar un alimento a la lista
#def agregar_alimento():
    # Cargar la información de alimentos desde el archivo JSON
    try:
        with open('alimentos.json', 'r') as file:
            alimentos = json.load(file)
    except FileNotFoundError:
        alimentos = {}
    categorias = {
        1: {"nombre": "Frutas y verduras", "unidades": [1, 2, 3, 4, 5]},
        2: {"nombre": "Proteínas", "unidades": [1, 2, 3]},
        3: {"nombre": "Carbohidratos", "unidades": [1, 2, 3, 6, 7, 8, 9]},
        4: {"nombre": "Lácteos", "unidades": [1, 2, 3]},
        5: {"nombre": "Grasas y aceites", "unidades": [1, 2, 3, 6, 7]},
        6: {"nombre": "Dulces y postres", "unidades": [1, 2, 3, 8, 10, 11, 12]},
        7: {"nombre": "Bebidas", "unidades": [6, 11, 12]}
    }

    unidades = {
        1: "kilogramos (kg)",
        2: "gramos (g)",
        3: "unidades (u.)",
        4: "manojos",
        5: "ramas",
        6: "libras (lb)",
        7: "onzas (oz)",
        8: "tazas",
        9: "gramos de harina",
        10: "litros (l)",
        11: "mililitros (ml)",
        12: "onzas fluidas (fl oz)"
    }

    print("Seleccione la categoría del alimento:")
    for key, value in categorias.items():
        print(f"{key}. {value['nombre']}")
    print("Introduzca el número de la categoría: ")
    categoria = obtener_opcion_valida(categorias.keys())

    print(f"Seleccione la unidad de medida para {categorias[categoria]['nombre']}:")
    medidas = categorias[categoria]['unidades']
    for key, value in unidades.items():
        if key in medidas:
            print(f"{key}. {value}")
    print(f"Introduzca el número de la unidad de medida para {categorias[categoria]['nombre']}:")
    unidad = obtener_opcion_valida(medidas)

    nombre = input(f"Para la categoría '{categorias[categoria]['nombre']}', introduzca el nombre del alimento: ")

    cantidad = float(input(f"Cuántas {unidades[unidad]} desea introducir de la categoría '{categorias[categoria]['nombre']}' y alimento '{nombre}': "))

    alimentos[nombre] = {
        'categoria': categorias[categoria]['nombre'],
        'unidad': unidades[unidad],
        'cantidad': cantidad
    }

    print(f"Agregar alimento: {alimentos[nombre]['categoria']} - {nombre} ({cantidad} {unidades[unidad]})")

    # Guardar información en un archivo JSON
    with open('alimentos.json', 'w') as file:
        json.dump(alimentos, file)

    return alimentos

def agregar_alimento():
    # Cargar la información de alimentos desde el archivo JSON
    try:
        with open('alimentos.json', 'r') as file:
            alimentos = json.load(file)
    except FileNotFoundError:
        alimentos = {}

    categorias = {
        1: {"nombre": "Frutas y verduras", "unidades": [1, 2, 3, 4, 5]},
        2: {"nombre": "Proteínas", "unidades": [1, 2, 3]},
        3: {"nombre": "Carbohidratos", "unidades": [1, 2, 3, 6, 7, 8, 9]},
        4: {"nombre": "Lácteos", "unidades": [1, 2, 3]},
        5: {"nombre": "Grasas y aceites", "unidades": [1, 2, 3, 6, 7]},
        6: {"nombre": "Dulces y postres", "unidades": [1, 2, 3, 8, 9, 10, 11, 12]},
        7: {"nombre": "Bebidas", "unidades": [1, 2, 3, 10, 11, 12]}
    }

    unidades = {
        1: "kilogramos (kg)",
        2: "gramos (g)",
        3: "unidades (u.)",
        4: "manojos",
        5: "ramas",
        6: "libras (lb)",
        7: "onzas (oz)",
        8: "tazas",
        9: "gramos de harina",
        10: "litros (l)",
        11: "mililitros (ml)",
        12: "onzas fluidas (fl oz)"
    }

    print("Seleccione la categoría del alimento:")
    for key, value in categorias.items():
        print(f"{key}. {value['nombre']}")
    print("Introduzca el número de la categoría: ")
    categoria = obtener_opcion_valida(categorias.keys())

    print(f"Seleccione la unidad de medida para {categorias[categoria]['nombre']}:")
    medidas = categorias[categoria]['unidades']
    for key, value in unidades.items():
        if key in medidas:
            print(f"{key}. {value}")
    print(f"Introduzca el número de la unidad de medida para {categorias[categoria]['nombre']}:")
    unidad = obtener_opcion_valida(medidas)

    nombre = input(f"Para la categoría '{categorias[categoria]['nombre']}', introduzca el nombre del alimento: ")

    cantidad = float(input(f"Cuántas {unidades[unidad]} desea introducir de la categoría '{categorias[categoria]['nombre']}' y alimento '{nombre}': "))

    precio = float(input(f"Introduzca el precio de '{nombre}' total de {unidades[unidad]}: "))

    valor_unitario = precio / cantidad

    alimentos[nombre] = {
        'categoria': categorias[categoria]['nombre'],
        'unidad': unidades[unidad],
        'cantidad': cantidad,
        'precio': precio,
        'valor_unitario': valor_unitario
    }

    print(f"Agregar alimento: {alimentos[nombre]['categoria']} - {nombre} ({cantidad} {unidades[unidad]}) - {valor_unitario:.2f} $/{unidades[unidad]}")

    # Guardar información en un archivo JSON
    with open('alimentos.json', 'w') as file:
        json.dump(alimentos, file)

    return alimentos

# Función para eliminar un alimento de la lista
# Función para eliminar un alimento de la lista
def eliminar_alimento(alimentos):
    # Cargar la información de alimentos desde el archivo JSON
    try:
        with open('alimentos.json', 'r') as file:
            alimentos = json.load(file)
    except FileNotFoundError:
        alimentos = {}

    # Mostrar la lista de alimentos
    print("Lista de alimentos:")
    for i, alimento in enumerate(alimentos.items()):
        nombre, info = alimento
        print(f"{i+1}. {info['categoria']}, '{nombre}': {info['cantidad']} {info['unidad']}")

    # Obtener el número de alimento a eliminar
    num_alimento = int(input("Seleccione el número del alimento que desea eliminar: "))
    while num_alimento not in range(1, len(alimentos)+1):
        print("Número de alimento no válido. Intente de nuevo.")
        num_alimento = int(input("Seleccione el número del alimento que desea eliminar: "))

    # Eliminar el alimento de la lista y guardarlo en el archivo de alimentos gastados
    nombre_alimento = list(alimentos.keys())[num_alimento-1]
    alimento_eliminado = alimentos.pop(nombre_alimento)

    # Guardar el alimento eliminado en el archivo alimentos_gastados.json
    alimentos_gastados = []
    try:
        with open('alimentos_gastados.json', 'r') as file:
            alimentos_gastados = json.load(file)
    except FileNotFoundError:
        pass

    alimentos_gastados.append(alimento_eliminado)
    with open('alimentos_gastados.json', 'w') as file:
        json.dump(alimentos_gastados, file)

    # Guardar la información actualizada de alimentos en el archivo JSON
    with open('alimentos.json', 'w') as file:
        json.dump(alimentos, file)

    print(f"Se ha eliminado '{nombre_alimento}' de la lista de alimentos.")



def ver_lista_alimentos(alimentos):
    # Cargar la información de alimentos desde el archivo JSON
    try:
        with open('alimentos.json', 'r') as file:
            alimentos = json.load(file)
    except FileNotFoundError:
        alimentos = {}

    # Ordenar los alimentos por categoría y nombre
    alimentos_ordenados = sorted(alimentos.items(), key=lambda x: (x[1]['categoria'], x[0]))

    # Mostrar la lista de alimentos ordenada
    print("Lista de alimentos:")
    for i, alimento in enumerate(alimentos_ordenados):
        nombre, info = alimento
        print(f"{i+1}. {info['categoria']}, '{nombre}': {info['cantidad']} {info['unidad']}")



# Función para mostrar los gastos en alimentos
def ver_gastos_alimentos():
    # Cargar la información de alimentos gastados desde el archivo JSON
    try:
        with open('alimentos_gastados.json', 'r') as file:
            alimentos_gastados = json.load(file)
    except FileNotFoundError:
        print("No se han registrado gastos en alimentos aún.")
        return

    # Mostrar la lista de alimentos gastados
    if not alimentos_gastados:
        print("No hay información de gastos en alimentos.")
    else:
        print("Lista de alimentos gastados:")
        for i, alimento in enumerate(alimentos_gastados):
            categoria = alimento.get('categoria', 'Desconocido')
            nombre = alimento.get('nombre', 'Desconocido')
            cantidad = alimento.get('cantidad', 'Desconocido')
            unidad = alimento.get('unidad', 'Desconocido')
            print(f"{i+1}. {categoria}, '{nombre}': {cantidad} {unidad}")




# Función para actualizar la información de los alimentos
def modificar_alimento(alimentos):
    # Cargar la información de alimentos desde el archivo JSON
    try:
        with open('alimentos.json', 'r') as file:
            alimentos = json.load(file)
    except FileNotFoundError:
        alimentos = {}

    # Mostrar la lista de alimentos
    print("Lista de alimentos:")
    for i, alimento in enumerate(alimentos.items()):
        nombre, info = alimento
        print(f"{i+1}. {info['categoria']}, '{nombre}': {info['cantidad']} {info['unidad']}")

    # Obtener el número de alimento a modificar
    num_alimento = int(input("Seleccione el número del alimento que desea modificar: "))
    while num_alimento not in range(1, len(alimentos)+1):
        print("Número de alimento no válido. Intente de nuevo.")
        num_alimento = int(input("Seleccione el número del alimento que desea modificar: "))

    # Seleccionar el alimento a modificar
    nombre_alimento = list(alimentos.keys())[num_alimento-1]
    alimento_modificar = alimentos[nombre_alimento]

    # Mostrar la información actual del alimento seleccionado
    print(f"Alimento seleccionado: {alimento_modificar['categoria']} - {nombre_alimento} ({alimento_modificar['cantidad']} {alimento_modificar['unidad']})")

    # Obtener la nueva información del alimento
    print("Ingrese la nueva información para el alimento")
    print(f"Categoría actual: {alimento_modificar['categoria']}")
    nueva_categoria = input("Introduzca la nueva categoría (dejar en blanco para no cambiar): ") or alimento_modificar['categoria']

    print(f"Nombre actual: {nombre_alimento}")
    nuevo_nombre = input("Introduzca el nuevo nombre (dejar en blanco para no cambiar): ") or nombre_alimento

    print(f"Unidad actual: {alimento_modificar['unidad']}")
    print(f"Cantidad actual: {alimento_modificar['cantidad']}")
    nueva_unidad = input("Introduzca la nueva unidad de medida (dejar en blanco para no cambiar): ") or alimento_modificar['unidad']
    nueva_cantidad = float(input("Introduzca la nueva cantidad (dejar en blanco para no cambiar): ") or alimento_modificar['cantidad'])

    # Crear un nuevo alimento con la información actualizada
    nuevo_alimento = {
        'categoria': nueva_categoria,
        'unidad': nueva_unidad,
        'cantidad': nueva_cantidad
    }

    # Actualizar la información del alimento seleccionado
    alimentos.pop(nombre_alimento)
    alimentos[nuevo_nombre] = nuevo_alimento

    # Actualizar la información de alimentos en el archivo JSON
    with open('alimentos.json', 'w') as file:
        json.dump(alimentos, file)

    # Mostrar la información del alimento modificado
    print(f"\n{'-'*30}")
    print("Información del alimento modificado:")
    print(f"Categoría: {nuevo_alimento['categoria']}")
    print(f"Nombre: {nuevo_nombre}")
    print(f"Cantidad: {nuevo_alimento['cantidad']} {nuevo_alimento['unidad']}")
    print(f"{'-'*30}")
import json
import os

# Función para validar la entrada del usuario en función de las opciones disponibles
def obtener_opcion_valida(opciones):
    while True:
        try:
            opcion = int(input())
            if opcion in opciones:
                return opcion
            else:
                raise ValueError
        except ValueError:
            print("Opción no válida, por favor ingrese un número válido.")

# Función que muestra el menú principal
def menu_principal():
    print("Menú principal:")
    print("1. Agregar alimento")
    print("2. Eliminar alimento")
    print("3. Ver lista de alimentos")
    print("4. Ver gastos en alimentos")
    print("5. Actualizar información de alimentos")
    print("6. Salir")
    while True:
        opcion = input("Seleccione una opción: ")
        if opcion in ['1', '2', '3', '4', '5', '6']:
            return int(opcion)
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


# Función principal que ejecuta el programa
def main():

    alimentos = {}
    alimentos_gastados = []

    while True:
        opcion = menu_principal()
        if opcion == 1:
            alimento_agregado = agregar_alimento()
            alimentos.update(alimento_agregado)
        elif opcion == 2:
            eliminar_alimento(alimentos)
        elif opcion == 3:
            ver_lista_alimentos(alimentos)
        elif opcion == 4:
            ver_gastos_alimentos()
        elif opcion == 5:
            modificar_alimento(alimentos)
        elif opcion == 6:
            break

# Función para agregar un alimento a la lista
#def agregar_alimento():
    # Cargar la información de alimentos desde el archivo JSON
    try:
        with open('alimentos.json', 'r') as file:
            alimentos = json.load(file)
    except FileNotFoundError:
        alimentos = {}
    categorias = {
        1: {"nombre": "Frutas y verduras", "unidades": [1, 2, 3, 4, 5]},
        2: {"nombre": "Proteínas", "unidades": [1, 2, 3]},
        3: {"nombre": "Carbohidratos", "unidades": [1, 2, 3, 6, 7, 8, 9]},
        4: {"nombre": "Lácteos", "unidades": [1, 2, 3]},
        5: {"nombre": "Grasas y aceites", "unidades": [1, 2, 3, 6, 7]},
        6: {"nombre": "Dulces y postres", "unidades": [1, 2, 3, 8, 10, 11, 12]},
        7: {"nombre": "Bebidas", "unidades": [6, 11, 12]}
    }

    unidades = {
        1: "kilogramos (kg)",
        2: "gramos (g)",
        3: "unidades (u.)",
        4: "manojos",
        5: "ramas",
        6: "libras (lb)",
        7: "onzas (oz)",
        8: "tazas",
        9: "gramos de harina",
        10: "litros (l)",
        11: "mililitros (ml)",
        12: "onzas fluidas (fl oz)"
    }

    print("Seleccione la categoría del alimento:")
    for key, value in categorias.items():
        print(f"{key}. {value['nombre']}")
    print("Introduzca el número de la categoría: ")
    categoria = obtener_opcion_valida(categorias.keys())

    print(f"Seleccione la unidad de medida para {categorias[categoria]['nombre']}:")
    medidas = categorias[categoria]['unidades']
    for key, value in unidades.items():
        if key in medidas:
            print(f"{key}. {value}")
    print(f"Introduzca el número de la unidad de medida para {categorias[categoria]['nombre']}:")
    unidad = obtener_opcion_valida(medidas)

    nombre = input(f"Para la categoría '{categorias[categoria]['nombre']}', introduzca el nombre del alimento: ")

    cantidad = float(input(f"Cuántas {unidades[unidad]} desea introducir de la categoría '{categorias[categoria]['nombre']}' y alimento '{nombre}': "))

    alimentos[nombre] = {
        'categoria': categorias[categoria]['nombre'],
        'unidad': unidades[unidad],
        'cantidad': cantidad
    }

    print(f"Agregar alimento: {alimentos[nombre]['categoria']} - {nombre} ({cantidad} {unidades[unidad]})")

    # Guardar información en un archivo JSON
    with open('alimentos.json', 'w') as file:
        json.dump(alimentos, file)

    return alimentos

def agregar_alimento():
    # Cargar la información de alimentos desde el archivo JSON
    try:
        with open('alimentos.json', 'r') as file:
            alimentos = json.load(file)
    except FileNotFoundError:
        alimentos = {}

    categorias = {
        1: {"nombre": "Frutas y verduras", "unidades": [1, 2, 3, 4, 5]},
        2: {"nombre": "Proteínas", "unidades": [1, 2, 3]},
        3: {"nombre": "Carbohidratos", "unidades": [1, 2, 3, 6, 7, 8, 9]},
        4: {"nombre": "Lácteos", "unidades": [1, 2, 3]},
        5: {"nombre": "Grasas y aceites", "unidades": [1, 2, 3, 6, 7]},
        6: {"nombre": "Dulces y postres", "unidades": [1, 2, 3, 8, 9, 10, 11, 12]},
        7: {"nombre": "Bebidas", "unidades": [1, 2, 3, 10, 11, 12]}
    }

    unidades = {
        1: "kilogramos (kg)",
        2: "gramos (g)",
        3: "unidades (u.)",
        4: "manojos",
        5: "ramas",
        6: "libras (lb)",
        7: "onzas (oz)",
        8: "tazas",
        9: "gramos de harina",
        10: "litros (l)",
        11: "mililitros (ml)",
        12: "onzas fluidas (fl oz)"
    }

    print("Seleccione la categoría del alimento:")
    for key, value in categorias.items():
        print(f"{key}. {value['nombre']}")
    print("Introduzca el número de la categoría: ")
    categoria = obtener_opcion_valida(categorias.keys())

    print(f"Seleccione la unidad de medida para {categorias[categoria]['nombre']}:")
    medidas = categorias[categoria]['unidades']
    for key, value in unidades.items():
        if key in medidas:
            print(f"{key}. {value}")
    print(f"Introduzca el número de la unidad de medida para {categorias[categoria]['nombre']}:")
    unidad = obtener_opcion_valida(medidas)

    nombre = input(f"Para la categoría '{categorias[categoria]['nombre']}', introduzca el nombre del alimento: ")

    cantidad = float(input(f"Cuántas {unidades[unidad]} desea introducir de la categoría '{categorias[categoria]['nombre']}' y alimento '{nombre}': "))

    precio = float(input(f"Introduzca el precio de '{nombre}' total de {unidades[unidad]}: "))

    valor_unitario = precio / cantidad

    alimentos[nombre] = {
        'categoria': categorias[categoria]['nombre'],
        'unidad': unidades[unidad],
        'cantidad': cantidad,
        'precio': precio,
        'valor_unitario': valor_unitario
    }

    print(f"Agregar alimento: {alimentos[nombre]['categoria']} - {nombre} ({cantidad} {unidades[unidad]}) - {valor_unitario:.2f} $/{unidades[unidad]}")

    # Guardar información en un archivo JSON
    with open('alimentos.json', 'w') as file:
        json.dump(alimentos, file)

    return alimentos

# Función para eliminar un alimento de la lista
# Función para eliminar un alimento de la lista
def eliminar_alimento(alimentos):
    # Cargar la información de alimentos desde el archivo JSON
    try:
        with open('alimentos.json', 'r') as file:
            alimentos = json.load(file)
    except FileNotFoundError:
        alimentos = {}

    # Mostrar la lista de alimentos
    print("Lista de alimentos:")
    for i, alimento in enumerate(alimentos.items()):
        nombre, info = alimento
        print(f"{i+1}. {info['categoria']}, '{nombre}': {info['cantidad']} {info['unidad']}")

    # Obtener el número de alimento a eliminar
    num_alimento = int(input("Seleccione el número del alimento que desea eliminar: "))
    while num_alimento not in range(1, len(alimentos)+1):
        print("Número de alimento no válido. Intente de nuevo.")
        num_alimento = int(input("Seleccione el número del alimento que desea eliminar: "))

    # Eliminar el alimento de la lista y guardarlo en el archivo de alimentos gastados
    nombre_alimento = list(alimentos.keys())[num_alimento-1]
    alimento_eliminado = alimentos.pop(nombre_alimento)

    # Guardar el alimento eliminado en el archivo alimentos_gastados.json
    alimentos_gastados = []
    try:
        with open('alimentos_gastados.json', 'r') as file:
            alimentos_gastados = json.load(file)
    except FileNotFoundError:
        pass

    alimentos_gastados.append(alimento_eliminado)
    with open('alimentos_gastados.json', 'w') as file:
        json.dump(alimentos_gastados, file)

    # Guardar la información actualizada de alimentos en el archivo JSON
    with open('alimentos.json', 'w') as file:
        json.dump(alimentos, file)

    print(f"Se ha eliminado '{nombre_alimento}' de la lista de alimentos.")



def ver_lista_alimentos(alimentos):
    # Cargar la información de alimentos desde el archivo JSON
    try:
        with open('alimentos.json', 'r') as file:
            alimentos = json.load(file)
    except FileNotFoundError:
        alimentos = {}

    # Ordenar los alimentos por categoría y nombre
    alimentos_ordenados = sorted(alimentos.items(), key=lambda x: (x[1]['categoria'], x[0]))

    # Mostrar la lista de alimentos ordenada
    print("Lista de alimentos:")
    for i, alimento in enumerate(alimentos_ordenados):
        nombre, info = alimento
        print(f"{i+1}. {info['categoria']}, '{nombre}': {info['cantidad']} {info['unidad']}")



# Función para mostrar los gastos en alimentos
def ver_gastos_alimentos():
    # Cargar la información de alimentos gastados desde el archivo JSON
    try:
        with open('alimentos_gastados.json', 'r') as file:
            alimentos_gastados = json.load(file)
    except FileNotFoundError:
        print("No se han registrado gastos en alimentos aún.")
        return

    # Mostrar la lista de alimentos gastados
    if not alimentos_gastados:
        print("No hay información de gastos en alimentos.")
    else:
        print("Lista de alimentos gastados:")
        for i, alimento in enumerate(alimentos_gastados):
            categoria = alimento.get('categoria', 'Desconocido')
            nombre = alimento.get('nombre', 'Desconocido')
            cantidad = alimento.get('cantidad', 'Desconocido')
            unidad = alimento.get('unidad', 'Desconocido')
            print(f"{i+1}. {categoria}, '{nombre}': {cantidad} {unidad}")




# Función para actualizar la información de los alimentos
def modificar_alimento(alimentos):
    # Cargar la información de alimentos desde el archivo JSON
    try:
        with open('alimentos.json', 'r') as file:
            alimentos = json.load(file)
    except FileNotFoundError:
        alimentos = {}

    # Mostrar la lista de alimentos
    print("Lista de alimentos:")
    for i, alimento in enumerate(alimentos.items()):
        nombre, info = alimento
        print(f"{i+1}. {info['categoria']}, '{nombre}': {info['cantidad']} {info['unidad']}")

    # Obtener el número de alimento a modificar
    num_alimento = int(input("Seleccione el número del alimento que desea modificar: "))
    while num_alimento not in range(1, len(alimentos)+1):
        print("Número de alimento no válido. Intente de nuevo.")
        num_alimento = int(input("Seleccione el número del alimento que desea modificar: "))

    # Seleccionar el alimento a modificar
    nombre_alimento = list(alimentos.keys())[num_alimento-1]
    alimento_modificar = alimentos[nombre_alimento]

    # Mostrar la información actual del alimento seleccionado
    print(f"Alimento seleccionado: {alimento_modificar['categoria']} - {nombre_alimento} ({alimento_modificar['cantidad']} {alimento_modificar['unidad']})")

    # Obtener la nueva información del alimento
    print("Ingrese la nueva información para el alimento")
    print(f"Categoría actual: {alimento_modificar['categoria']}")
    nueva_categoria = input("Introduzca la nueva categoría (dejar en blanco para no cambiar): ") or alimento_modificar['categoria']

    print(f"Nombre actual: {nombre_alimento}")
    nuevo_nombre = input("Introduzca el nuevo nombre (dejar en blanco para no cambiar): ") or nombre_alimento

    print(f"Unidad actual: {alimento_modificar['unidad']}")
    print(f"Cantidad actual: {alimento_modificar['cantidad']}")
    nueva_unidad = input("Introduzca la nueva unidad de medida (dejar en blanco para no cambiar): ") or alimento_modificar['unidad']
    nueva_cantidad = float(input("Introduzca la nueva cantidad (dejar en blanco para no cambiar): ") or alimento_modificar['cantidad'])

    # Crear un nuevo alimento con la información actualizada
    nuevo_alimento = {
        'categoria': nueva_categoria,
        'unidad': nueva_unidad,
        'cantidad': nueva_cantidad
    }

    # Actualizar la información del alimento seleccionado
    alimentos.pop(nombre_alimento)
    alimentos[nuevo_nombre] = nuevo_alimento

    # Actualizar la información de alimentos en el archivo JSON
    with open('alimentos.json', 'w') as file:
        json.dump(alimentos, file)

    # Mostrar la información del alimento modificado
    print(f"\n{'-'*30}")
    print("Información del alimento modificado:")
    print(f"Categoría: {nuevo_alimento['categoria']}")
    print(f"Nombre: {nuevo_nombre}")
    print(f"Cantidad: {nuevo_alimento['cantidad']} {nuevo_alimento['unidad']}")
    print(f"{'-'*30}")



if __name__ == "__main__":
    main()

