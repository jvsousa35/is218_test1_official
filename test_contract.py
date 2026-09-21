"""Supplied acceptance checks for the published integer cases. Keep unchanged."""

import pytest

from calculator import add, subtract


@pytest.mark.parametrize("a,b,expected", [(2, 3, 5), (7, 0, 7), (-4, 1, -3)])
def test_add_contract(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [(5, 3, 2), (3, 5, -2), (7, 0, 7)])
def test_subtract_contract(a, b, expected):
    assert subtract(a, b) == expected
