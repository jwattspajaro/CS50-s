import csv
import sys

# Verifica si hay exactamente dos argumentos de línea de comandos
if len(sys.argv) != 3:
    print("Uso: scourgify.py input.csv output.csv")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        # Escribe la línea de encabezado en el archivo de salida
        writer.writeheader()

        for row in reader:
            # Separa el nombre en nombre y apellido
            last, first = row['name'].split(', ')
            house = row['house']

            # Escribe una nueva fila con los campos modificados en el archivo de salida
            writer.writerow({'first': first, 'last': last, 'house': house})

except FileNotFoundError:
    print(f"Error: No se puede leer el archivo {input_file}")
    sys.exit(1)
