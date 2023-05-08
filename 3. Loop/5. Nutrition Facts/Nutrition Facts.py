# Diccionario que almacena los nombres de las frutas y sus calorías correspondientes
FRUITS = {
    "apple": 130,
    "avocado": 50,
    "kiwifruit": 90,
    "pear": 100,
    "sweet cherries": 100,
}

# Función principal para obtener la cantidad de calorías de una fruta
def main():
    # Solicita al usuario que ingrese el nombre de una fruta
    fruit = input("Fruit: ").strip().lower()
    # Obtiene las calorías de la fruta ingresada usando el diccionario FRUITS
    calories = FRUITS.get(fruit)
    # Si la fruta está en el diccionario, imprime las calorías
    if calories:
        print(calories)

# Si el script se ejecuta directamente (no importado como módulo)
if __name__ == "__main__":
    # Llama a la función principal para iniciar la consulta de calorías
    main()
