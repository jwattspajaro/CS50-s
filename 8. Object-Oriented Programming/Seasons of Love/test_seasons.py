from seasons import convert

def test_convert():
    # Caso de prueba 1: Verificar si la función convert retorna el valor correcto para 10477 días
    assert convert(10477) == "Quince millones, ochenta y seis mil, ochocientos ochenta minutos"

    # Caso de prueba 2: Verificar si la función convert retorna el valor correcto para 365 días
    assert convert(365) == "Quinientos veinticinco mil seiscientos minutos"
