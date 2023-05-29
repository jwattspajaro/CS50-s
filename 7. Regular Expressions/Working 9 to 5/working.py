# El código importa el módulo re para trabajar con expresiones regulares.
# La función main solicita al usuario que ingrese las horas de trabajo en un formato de 12 horas y luego llama a la función 
# convert con las horas ingresadas como argumento. Luego imprime el resultado de la función convert.
# La función convert recibe una cadena de texto que representa un rango de horas de trabajo en formato de 12 horas. 
# Utiliza una expresión regular para extraer las horas, los minutos y los indicadores AM/PM de la cadena de texto. 
# Luego realiza las conversiones necesarias para convertir las horas al formato de 24 horas. 
# Si las horas y los minutos están dentro de los rangos válidos, devuelve el rango de horas convertido en formato de 24 horas. 
# De lo contrario, lanza una excepción con un mensaje de error.
# La condición if __name__ == "__main__": se utiliza para ejecutar la función main si el archivo se está ejecutando directamente 
# y no siendo importado como un módulo.

import re  # Importamos el módulo 're' para trabajar con expresiones regulares

def main():
    # Solicitamos al usuario que ingrese las horas de trabajo en formato de 12 horas
    print(convert(input("Horas: ")))

def convert(s):
    # Definimos una expresión regular para extraer las horas y los indicadores AM/PM
    regex = r'(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)'

    # Realizamos la búsqueda utilizando la expresión regular
    match = re.search(regex, s)

    # Si se encuentra una coincidencia, convertimos las horas al formato de 24 horas
    if match:
        hour1, minute1, am_pm1, hour2, minute2, am_pm2 = match.groups()
        hour1, hour2 = int(hour1), int(hour2)
        minute1, minute2 = int(minute1 or 0), int(minute2 or 0)

        if am_pm1 == 'PM' and hour1 != 12:
            hour1 += 12
        if am_pm1 == 'AM' and hour1 == 12:
            hour1 = 0
        if am_pm2 == 'PM' and hour2 != 12:
            hour2 += 12
        if am_pm2 == 'AM' and hour2 == 12:
            hour2 = 0

        if 0 <= hour1 < 24 and 0 <= hour2 < 24 and 0 <= minute1 < 60 and 0 <= minute2 < 60:
            return f"{hour1:02}:{minute1:02} to {hour2:02}:{minute2:02}"
        else:
            raise ValueError("Formato de hora inválido")
    else:
        raise ValueError("Formato de entrada inválido")

if __name__ == "__main__":
    main()
