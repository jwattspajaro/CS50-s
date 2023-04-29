#WRITING IN ALL CAPS IS LIKE YELLING.
#Best to use your “indoor voice” sometimes, writing entirely in lowercase.
#In a file called indoor.py, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.
#Hints
#Recall that input returns a str, per docs.python.org/3/library/functions.html#input.
#Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods. ...

def indoor_voice():
    # Solicita al usuario que ingrese una cadena
    user_input = input("Por favor ingrese una cadena: ")
    # Convierte la cadena ingresada a minúsculas
    lowercase_input = user_input.lower()
    # Imprime la cadena en minúsculas
    print(lowercase_input)

# Verifica si el archivo se está ejecutando como un programa principal
if __name__ == '__main__':
    # Llamada a la función indoor_voice
    indoor_voice()
