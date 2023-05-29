# Importamos la función "email" de la biblioteca "validators"
from validators import email

# Solicitamos al usuario que ingrese una dirección de correo electrónico
direccion_correo = input("Por favor, ingrese una dirección de correo electrónico: ")

# Verificamos si la dirección de correo electrónico ingresada es válida usando la función "email"
es_valido = email(direccion_correo)

# Imprimimos "Válido" si la dirección de correo electrónico es válida, de lo contrario imprimimos "Inválido"
if es_valido:
    print("Valid")
else:
    print("Invalid")
