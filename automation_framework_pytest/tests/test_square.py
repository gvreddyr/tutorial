import pytest
import math


@pytest.mark.math
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 6


@pytest.mark.math
def test_square():
    num = 7
    assert num*num == 48


@pytest.mark.math
def test_equality():
    assert 10 == 11
