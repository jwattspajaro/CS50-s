###Debido a que los emoji no son tan fáciles de escribir como el texto, al menos en computadoras portátiles y de escritorio, algunos programas admiten "códigos", mediante los cuales puede escribir, por ejemplo, :thumbs_up: que se convertirán automáticamente a 👍. Algunos programas también admiten alias, por lo que puede escribir de manera más sucinta, por ejemplo, :thumbsup: que también se convertirá automáticamente a 👍.  

Consulta carpedm20.github.io/emoji/all.html?enableList=enable_list_alias para obtener una lista de códigos con alias.

###En un archivo llamado emojize.py, implemente un programa que solicite al usuario un stren inglés y luego emita la versión "emojizada" de ese str, convirtiendo cualquier código (o alias) en su emoji correspondiente.

Sugerencias
Tenga en cuenta que el emojimódulo viene con dos funciones, según pypi.org/project/emoji, una de las cuales es emojize, que toma un parámetro con nombre opcional llamado language. Puedes instalarlo con:
pip install emoji

####Manifestación Cómo probar
Aquí le mostramos cómo probar su código manualmente:

Ejecute su programa con python emojize.py. Escriba :1st_place_medal:y presione Entrar. Su programa debe generar:
Output: 🥇
Ejecute su programa con python emojize.py. Escriba :money_bag:y presione Entrar. Su programa debe generar:
Output: 💰
Ejecute su programa con python emojize.py. Escriba :smile_cat:y presione Entrar. Su programa debe generar:
Output: 😸
