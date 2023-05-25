import sys
import os
import csv
from tabulate import tabulate

def main():
    # Comprueba si se proporciona exactamente un argumento de línea de comandos
    if len(sys.argv) != 2:
        print("Número insuficiente de argumentos de línea de comandos")
        sys.exit(1)

    file_path = sys.argv[1]

    # Comprueba si el archivo tiene una extensión .csv
    if not file_path.endswith(".csv"):
        print("No es un archivo CSV")
        sys.exit(1)
