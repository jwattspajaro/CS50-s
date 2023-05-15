## Adios, adios
### En [The Sound of Music](https://en.wikipedia.org/wiki/The_Sound_of_Music_(film)) , hay una canción cantada principalmente en inglés,
[So Long, Farewell](https://www.youtube.com/watch?v=Qy9_lfjQopU) , con esta [letra](https://www.lyrics.com/lyric/3998488/Julie+Andrews/So+Long%2C+Farewell) , en la que “adieu” significa “adiós” en francés:

    Adieu, adieu, a yieu y yieu y yieu

    Por supuesto, la línea no es gramaticalmente correcta, ya que normalmente se escribiría (con una [coma de Oxford](https://en.wikipedia.org/wiki/Serial_comma) ) como:

    Adieu, adieu, a yieu, yieu, y yieu

Para ser justos, "yieu" ni siquiera es una palabra; simplemente rima con "usted"!

En un archivo llamado adieu.py, implemente un programa que solicite nombres al usuario, uno por línea, hasta que el usuario ingrese control-d. Suponga que el usuario ingresará al menos un nombre. Luego despídase de esos nombres, separando dos nombres con uno and, tres nombres con dos comas y uno and, y
nombres con
comas y uno and, como se muestra a continuación:

    Adieu, adieu, a Liesl
    Adieu, adieu, a Liesl y Friedrich
    Adieu, adieu, a
    Liesl, Friedrich y Louisa Adieu, adieu, a Liesl, Friedrich, Louisa y Kurt
    Adieu, adieu, a Liesl, Friedrich, Louisa, Kurt , y Brigitta
    Adieu, adieu, a Liesl, Friedrich, Louisa, Kurt, Brigitta y Marta
    Adieu, adieu, a Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta y Gretl

**Sugerencias**
Tenga en cuenta que el inflectmódulo viene con bastantes métodos, según [pypi.org/project/inflect](https://pypi.org/project/inflect/) . Puedes instalarlo con:
pip install inflect
