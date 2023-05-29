from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(7)
    assert jar.size == 12

    try:
        jar.deposit(1)
    except ValueError as e:
        assert str(e) == "Cannot deposit that many cookies."

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5
    jar.withdraw(3)
    assert jar.size == 2

    try:
        jar.withdraw(5)
    except ValueError as e:
        assert str(e) == "Cannot withdraw that many cookies."
