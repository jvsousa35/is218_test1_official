from calculator import subtract


def test_subtract():
    assert subtract(5, 3) == 2


def test_subtract_negative_result():
    assert subtract(3, 5) == -2


def test_subtract_zero():
    assert subtract(7, 0) == 7
