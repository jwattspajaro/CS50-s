import pytest
from working import convert

# Prueba para el formato sin minutos
def test_no_minutes_format():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

# Prueba para el formato con minutos
def test_with_minutes_format():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

# Prueba para una hora de inicio en PM y una hora de finalización en AM
def test_pm_to_am():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

# Prueba para horas y minutos válidos
def test_valid_hours_and_minutes():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

# Prueba para un formato inválido
def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

# Prueba para un separador incorrecto
def test_wrong_separator():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

# Prueba para una entrada inválida
def test_invalid_input():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
 """       
 El código utiliza el módulo pytest para realizar pruebas unitarias en la función convert del archivo working.py.

Cada función de prueba utiliza el decorador @pytest.mark para indicar que es una prueba unitaria. Se utilizan diferentes casos de prueba para verificar el comportamiento de la función convert en diferentes situaciones.

Las pruebas incluyen casos como el formato sin minutos, el formato con minutos, una hora de inicio en PM y una hora de finalización en AM, horas y minutos válidos, formato inválido, separador incorrecto y entrada inválida. Se utiliza la aserción assert para verificar si el resultado de la función convert coincide con el valor esperado. En algunos casos, se utiliza pytest.raises para verificar si se lanza una excepción específica.

Para ejecutar las pruebas, se puede utilizar el comando pytest en la línea de comandos en el directorio que contiene el archivo de prueba.
"""
