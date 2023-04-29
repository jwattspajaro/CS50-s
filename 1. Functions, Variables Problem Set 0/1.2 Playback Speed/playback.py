#elocidad de reproducción
#Algunas personas tienen la costumbre de dar conferencias hablando con bastante rapidez, 
# y sería bueno reducir la velocidad, al estilo de la velocidad de reproducción de 0,75 de YouTube,
# o incluso hacer que hagan una pausa entre palabras.
# En un archivo llamado playback.py, 
# mplemente un programa en Python que solicite al usuario una entrada y 
# luego envíe esa misma entrada, reemplazando cada espacio con ...(es decir, tres puntos).


# Pide al usuario que introduzca una frase
frase = input("Introduce una frase: ")

# Divide la frase en palabras utilizando el método split
palabras = frase.split(" ")

# Une las palabras con el separador "..."
resultado = "...".join(palabras)

# Imprime el resultado final
print(resultado)
