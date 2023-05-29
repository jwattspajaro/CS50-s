from datetime import date
import inflect
import sys
import operator

p = inflect.engine()

def main():
    try:
        dob = input("Fecha de Nacimiento (YYYY-MM-DD): ")
        # date.fromisoformat(dob) verificará si dob es una fecha válida o no
        diferencia = operator.sub(date.today(), date.fromisoformat(dob))
        print(convert(diferencia.days))
    except ValueError:
        sys.exit("Fecha inválida. Por favor, utiliza el formato YYYY-MM-DD.")

def convert(tiempo):
    # Calcula el número de minutos a partir del tiempo de entrada (en días)
    minutos = tiempo * 24 * 60
    # Convierte el número de minutos a palabras y capitaliza la primera letra
    return f"{(p.number_to_words(minutos, andword='')).capitalize()} minutos"

if __name__ == "__main__":
    main()
