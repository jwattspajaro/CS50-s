import tempfile
import os
import json

def agregar_alimento(file_path, nombre, categoria, unidad, cantidad, precio):
    with open(file_path, 'r') as f:
        alimentos = json.load(f)

    valor_unitario = precio / cantidad if cantidad != 0 else float('inf')

    alimentos[nombre] = {
        'categoria': categoria,
        'unidad': unidad,
        'cantidad': cantidad,
        'precio': precio,
        'valor_unitario': round(valor_unitario, 2),
    }

    with open(file_path, 'w') as f:
        json.dump(alimentos, f)

    return alimentos


def eliminar_alimento(file_path, alimentos, nombre_alimento):
    with open(file_path, 'r') as f:
        alimentos = json.load(f)

    if nombre_alimento in alimentos:
        del alimentos[nombre_alimento]

    with open(file_path, 'w') as f:
        json.dump(alimentos, f)

    return alimentos

with tempfile.TemporaryDirectory() as tempdir:
    # Crear un archivo de prueba con un conjunto de alimentos
    alimentos_test = {
        'Manzanas': {'categoria': 'Frutas y verduras', 'unidad': 'kilogramos (kg)', 'cantidad': 1.5, 'precio': 3.50, 'valor_unitario': 2.33},
        'Plátanos': {'categoria': 'Frutas y verduras', 'unidad': 'kilogramos (kg)', 'cantidad': 1.0, 'precio': 2.00, 'valor_unitario': 2.00},
        'Arroz': {'categoria': 'Carbohidratos', 'unidad': 'kilogramos (kg)', 'cantidad': 0.5, 'precio': 1.50, 'valor_unitario': 3.00},
        'Pollo': {'categoria': 'Proteínas', 'unidad': 'kilogramos (kg)', 'cantidad': 0.75, 'precio': 5.00, 'valor_unitario': 6.67},
    }
    test_file_path = os.path.join(tempdir, 'test_alimentos.json')
    with open(test_file_path, 'w') as f:
        json.dump(alimentos_test, f)

    # Eliminar un alimento del archivo de prueba y comprobar si se eliminó correctamente
    alimentos = eliminar_alimento(test_file_path, alimentos_test, 'Plátanos')
    assert 'Plátanos' not in alimentos
    assert len(alimentos) == 3

    # Eliminar otro alimento del archivo de prueba y comprobar si se eliminó correctamente
    alimentos = eliminar_alimento(test_file_path, alimentos, 'Arroz')
    assert 'Arroz' not in alimentos
    assert len(alimentos) == 2

    # Agregar un alimento al archivo de prueba
    alimentos = agregar_alimento(test_file_path, 'Papa', 'Frutas y verduras', 'kilogramos (kg)', 1.0, 2.0)
    assert 'Papa' in alimentos
    assert len(alimentos) == 3

