### Week 7 Regular Expressions

#### Video: https://youtu.be/hy3sd9MOAcc
#### https://cs50.harvard.edu/python/2022/weeks/7/
#### ejercicios: https://cdn.cs50.net/python/2022/x/lectures/7/src7/

Problem Set 7
What to Do
Log into code.cs50.io, which is a cloud-based version of Visual Studio Code (VS Code) that provides you with your very own “codespace” with everything that you need for the course pre-installed. No need to download and install VS Code or Python on your own Mac or PC!
Execute update50 in your codespace’s terminal window to ensure that your codespace is up-to-date; if prompted, click Rebuild now.
Submit all of the problems below:

- [**NUMB3RS**](https://github.com/jwattspajaro/CS50-s/tree/main/7.%20Regular%20Expressions/NUMB3RS)
- **[Watch on YouTube](https://github.com/jwattspajaro/CS50-s/tree/main/7.%20Regular%20Expressions/Watch%20on%20YouTube)**
- **[Working 9 to 5](https://github.com/jwattspajaro/CS50-s/tree/main/7.%20Regular%20Expressions/Working%209%20to%205)**
- **[Regular, um, Expressions](https://github.com/jwattspajaro/CS50-s/tree/main/7.%20Regular%20Expressions/Regular%2C%20um%2C%20Expressions)**
- **[Response Validation](https://github.com/jwattspajaro/CS50-s/tree/main/7.%20Regular%20Expressions/Response%20Validation)**

Las expresiones regulares en Python son una poderosa herramienta para trabajar con patrones en cadenas de texto. Te explicaré cómo funcionan las expresiones regulares en Python:

Importar el módulo re: Para utilizar expresiones regulares en Python, primero debes importar el módulo re. Puedes hacerlo con la siguiente línea de código: import re.

Crear una expresión regular: Una expresión regular es un patrón que defines para buscar en una cadena de texto. Se utiliza una sintaxis especial para construir el patrón de búsqueda. Por ejemplo, puedes crear una expresión regular para encontrar direcciones de correo electrónico o números de teléfono en un texto.

Utilizar métodos de búsqueda: El módulo re proporciona varios métodos para buscar y trabajar con expresiones regulares en Python. Algunos de los métodos más comunes son:

re.search(pattern, string): Busca el patrón en la cadena de texto y devuelve un objeto match si encuentra una coincidencia. Puedes utilizar los métodos del objeto match para obtener información sobre la coincidencia encontrada.
re.match(pattern, string): Busca el patrón al comienzo de la cadena de texto y devuelve un objeto match si encuentra una coincidencia.
re.findall(pattern, string): Busca todas las coincidencias del patrón en la cadena de texto y devuelve una lista con todas las coincidencias encontradas.
re.sub(pattern, repl, string): Busca todas las coincidencias del patrón en la cadena de texto y las reemplaza con el texto especificado en repl.
Patrones y metacaracteres: Los patrones en las expresiones regulares se construyen utilizando caracteres literales y metacaracteres. Los metacaracteres son caracteres especiales que tienen un significado especial en las expresiones regulares. Algunos metacaracteres comunes son:

#### .: Coincide con cualquier carácter excepto una nueva línea.
#### *: Coincide con cero o más repeticiones del elemento anterior.
#### +: Coincide con una o más repeticiones del elemento anterior.
#### ?: Coincide con cero o una repetición del elemento anterior.
#### \d: Coincide con cualquier dígito.
#### \w: Coincide con cualquier carácter alfanumérico.
#### \s: Coincide con cualquier espacio en blanco.
#### []: Define un conjunto de caracteres permitidos.
#### (): Agrupa elementos y captura la coincidencia encontrada.

Estos son solo algunos ejemplos de metacaracteres, y hay muchos más disponibles en las expresiones regulares de Python.

Modificadores y banderas: Los modificadores y banderas se utilizan para realizar ajustes en el comportamiento de las expresiones regulares. Por ejemplo, la bandera re.IGNORECASE se puede usar para hacer que una búsqueda sea insensible a mayúsculas y minúsculas.
