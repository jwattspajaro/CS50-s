from numb3rs import validate  # Importamos la función 'validate' desde el archivo 'numb3rs.py'

def test_validate():
    # Verificar si la función devuelve True para una dirección IPv4 válida
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.4") == True
    assert validate("11.99.22.88") == True
    assert validate("249.249.249.249") == True

    # Verificar si la función devuelve False para una dirección IPv4 no válida
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("199.911.288.882") == False
    
#El código importa la función validate desde el archivo numb3rs.py utilizando la instrucción from numb3rs import validate.
#A continuación, se define la función test_validate que se encarga de realizar pruebas para validar la función validate.
#En las pruebas, se utilizan aserciones (assert) para verificar si la función validate devuelve el resultado esperado para diferentes casos de prueba. 
# Se comprueba si la función devuelve True para direcciones IPv4 válidas y se comprueba si devuelve False para direcciones IPv4 no válidas.
