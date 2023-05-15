## Cartas de Frank, Ian y Glen
### [FIGlet](https://en.wikipedia.org/wiki/FIGlet) , llamado así por las [cartas de Frank, Ian y Glen](http://www.figlet.org/faq.html) , es un programa de principios de la década de 1990 para hacer letras grandes a partir de texto ordinario, una forma de arte [ASCII](https://en.wikipedia.org/wiki/ASCII_art) :

 _ _ _          _   _     _
 
| (_) | _____  | |_| |__ (_)___

| | | |/ / _ \ | __| '_ \| / __|

| | |   <  __/ | |_| | | | \__ \

|_|_|_|\_\___|  \__|_| |_|_|___/

#### Entre las fuentes admitidas por FIGlet se encuentran las de [https://figlet.org/examples.html](http://www.figlet.org/examples.html).

#### Desde entonces, FIGlet ha sido portado a Python como un módulo llamado [pyfiglet](https://pypi.org/project/pyfiglet/0.7/)

#### En un archivo llamado figlet.py, implemente un programa que:

⚫ Espera cero o dos argumentos de línea de comandos:

    ⚫ Cero si el usuario desea generar texto en una fuente aleatoria.
    
    ⚫ Dos si el usuario desea generar texto en una fuente específica, en cuyo caso el primero de los dos debe ser -fo --font, y el segundo de los dos debe ser el nombre de la fuente.

⚫ Solicita al usuario una strde texto.

⚫ Muestra ese texto en la fuente deseada.

⚫ Si el usuario proporciona dos argumentos de línea de comandos y el primero no es -fo --fontel segundo no es el nombre de una fuente, el programa debería salir sys.exitcon un mensaje de error.

#### Sugerencias

        Puede instalar pyfigletcon:
pip install pyfiglet
La documentación de pyfiglet no es muy clara, pero puede usar el módulo de la siguiente manera:

    from pyfiglet import Figlet
    figlet = Figlet()
    
A continuación, puede obtener una listde las fuentes disponibles con un código como este:

    figlet.getFonts()
    
Puede configurar la fuente con un código como este, donde festá el nombre de la fuente como str:

    figlet.setFont(font=f)
    
Y puede generar texto en esa fuente con un código como este, en el que sestá ese texto como str:

    print(figlet.renderText(s))
    
Tenga en cuenta que el randommódulo viene con bastantes funciones, 
según [docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html) .
Manifestación

**Cómo probar**
Aquí le mostramos cómo probar su código manualmente:

**Ejecute su programa con python figlet.py test. Su programa debería salir vía sys.exite imprimir un mensaje de error:**

    Invalid usage
    
**Ejecute su programa con python figlet.py -a slant. Su programa debería salir vía sys.exite imprimir un mensaje de error:**

    Invalid usage
    
**Ejecute su programa con python figlet.py -f invalid_font. Su programa debería salir vía sys.exite imprimir un mensaje de error:**

  Invalid usage
  
**Ejecute su programa con python figlet.py -f slant. tipo CS50_ Su programa debe imprimir lo siguiente:**

   ___________ __________ 
   
  / ____/ ___// ____/ __ \
  
 / /    \__ \/___ \/ / / /
 
/ /___ ___/ /___/ / /_/ / 

\____//____/_____/\____/ 

**Ejecute su programa con python figlet.py -f rectangles. tipo Hello, world_ Su programa debe imprimir lo siguiente:**

 _____     _ _                        _   _ 
 
|  |  |___| | |___      _ _ _ ___ ___| |_| |

|     | -_| | | . |_   | | | | . |  _| | . |

|__|__|___|_|_|___| |  |_____|___|_| |_|___|
                  |_|                       
**Ejecute su programa con python figlet.py -f alphabet. tipo Moo_ Su programa debe imprimir lo siguiente:**

M   M 

MM MM  

M M M ooo ooo 

M   M o o o o 

M   M ooo ooo                     
