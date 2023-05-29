import pytest
from um import count

# Prueba para una sola aparición de "um"
def test_single_um():
    assert count("hello, um, world") == 1

# Prueba para cero apariciones de "um"
def test_zero_um():
    assert count("yummy") == 0

# Prueba para múltiples apariciones de "um" en diferentes casos
def test_multiple_um():
    assert count("Um, I think, um, it is, UM, quite interesting.") == 3

# Prueba para "um" como parte de una palabra
def test_um_in_word():
    assert count("The hummus is yummy.") == 0

# Prueba para "um" seguido de signos de puntuación
def test_um_with_punctuation():
    assert count("Um, is this the right way? um...") == 2
