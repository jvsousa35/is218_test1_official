from calculator import add


def test_add():
    assert add(2, 3) == 5


def test_add_zero():
    assert add(7, 0) == 7


def test_add_negative():
    assert add(-4, 1) == -3
