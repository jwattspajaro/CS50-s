# Define una función que toma una cadena como entrada y devuelve la cantidad de dinero correspondiente
def get_money_amount(input_str):
    # Comprueba si la entrada es igual a "Hello"
    if input_str == "Hello":
        # Devuelve la cadena "$0" si la entrada es igual a "Hello"
        return "$0"
    # Comprueba si la entrada es igual a "Hello, Newman"
    elif input_str == "Hello, Newman":
        # Devuelve la cadena "$0" si la entrada es igual a "Hello, Newman"
        return "$0"
    # Comprueba si la entrada es igual a "How you doing?"
    elif input_str == "How you doing?":
        # Devuelve la cadena "$20" si la entrada es igual a "How you doing?"
        return "$20"
    # Comprueba si la entrada es igual a "What's happening?"
    elif input_str == "What's happening?":
        # Devuelve la cadena "$100" si la entrada es igual a "What's happening?"
        return "$100"
    else:
        # Devuelve "Invalid input" si la entrada no coincide con ninguna de las cadenas anteriores
        return "Invalid input"

# Muestra una solicitud de entrada al usuario y lee la entrada desde la consola
user_input = input("Enter your message: ")

# Llama a la función get_money_amount con la entrada del usuario como argumento y muestra el resultado en la consola
print(get_money_amount(user_input))
