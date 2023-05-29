import json
import pytest

def agregar_alimento(nombre=None, categoria=None, unidad=None, cantidad=0, precio=0):
    alimentos = {}

    if nombre and categoria and unidad:
        valor_unitario = 0
        if cantidad != 0:
            valor_unitario = precio / cantidad

        alimentos[nombre] = {
            'categoria': categoria,
            'unidad': unidad,
            'cantidad': cantidad,
            'precio': precio,
            'valor_unitario': valor_unitario
        }

    return alimentos



def test_funcion_agregar_alimento():
    # Casos de prueba de la función agregar_alimento
    # Caso 1: Se agrega un alimento válido
    alimentos = agregar_alimento()
    assert 'Manzana' in alimentos
    assert alimentos['Manzana']['categoria'] == 'Frutas y verduras'
    assert alimentos['Manzana']['unidad'] == 'kilogramos (kg)'
    assert alimentos['Manzana']['cantidad'] == 1.5
    assert alimentos['Manzana']['precio'] == 2.5
    assert alimentos['Manzana']['valor_unitario'] == 1.67

    # Caso 2: Se agrega un alimento con cantidad cero
    alimentos = agregar_alimento()
    assert 'Zanahoria' in alimentos
    assert alimentos['Zanahoria']['categoria'] == 'Frutas y verduras'
    assert alimentos['Zanahoria']['unidad'] == 'kilogramos (kg)'
    assert alimentos['Zanahoria']['cantidad'] == 0
    assert alimentos['Zanahoria']['precio'] == 1.5
    assert alimentos['Zanahoria']['valor_unitario'] == float('inf')

    # Caso 3: Se agrega un alimento con precio cero
    alimentos = agregar_alimento()
    assert 'Leche' in alimentos
    assert alimentos['Leche']['categoria'] == 'Lácteos'
    assert alimentos['Leche']['unidad'] == 'litros (l)'
    assert alimentos['Leche']['cantidad'] == 2
    assert alimentos['Leche']['precio'] == 0
    assert alimentos['Leche']['valor_unitario'] == 0

    # Caso 4: Se agrega un alimento con nombre vacío
    alimentos = agregar_alimento()
    assert '' not in alimentos

    # Caso 5: Se agrega un alimento con una categoría inexistente
    alimentos = agregar_alimento()
    assert 'Tomate' in alimentos
    assert alimentos['Tomate']['categoria'] == ''
    assert alimentos['Tomate']['unidad'] == 'kilogramos (kg)'
    assert alimentos['Tomate']['cantidad'] == 0.5
    assert alimentos['Tomate']['precio'] == 1.5
    assert alimentos['Tomate']['valor_unitario'] == 3

    # Caso 6: Se agrega un alimento con una unidad de medida inexistente
    alimentos = agregar_alimento()
    assert 'Arroz' in alimentos
    assert alimentos['Arroz']['categoria'] == 'Carbohidratos'
    assert alimentos['Arroz']['unidad'] == ''
    assert alimentos['Arroz']['cantidad'] == 1
    assert alimentos['Arroz']['precio'] == 2
    assert alimentos['Arroz']['valor_unitario'] == 2
alimentos = agregar_alimento(nombre='Manzana', categoria='Frutas y verduras', unidad='kilogramos (kg)', cantidad=1.5, precio=2.5)
