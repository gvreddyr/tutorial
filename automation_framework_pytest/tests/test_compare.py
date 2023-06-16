import pytest


@pytest.mark.math
def test_greater():
    num = 100
    assert num > 100


@pytest.mark.math
def test_greater_equal():
    num = 100
    assert num >= 100


@pytest.mark.math
def test_less():
    num = 100
    assert num < 200
