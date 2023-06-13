import pytest
from calc import *


class TestCalc:
    @pytest.mark.parametrize("input_args, expected", [(('2', 3), None), ((2, '4'), None), ((2, 6), 8), ((2, 0), 2),
                                                      ((2, 3, 4), 9), ((2, 3, 4, 5, 6, 7, 8, 9, 10), 54), ((1, ), None)])
    def test_calc_add(self, input_args, expected):
        s = add(*input_args)
        assert s == expected, "Addition failed"

    @pytest.mark.parametrize("input_args, expected",
                             [((3, 2), 1), ((4, 2), 2), ((2, 6), -4), ((2, 0), 2), (('2', 0), None), ((1,), None)])
    def test_calc_sub(self, input_args, expected):
        s = sub(*input_args)
        assert s == expected, "Subtraction failed"

    @pytest.mark.parametrize("input_args, expected", [((6, 3), 2), ((4, 2), 2), ((4, ), None)])
    def test_calc_div(self, input_args, expected):
        s = div(*input_args)
        assert s == expected, "Division failed"

    @pytest.mark.parametrize("input_args,expected", [((2, 3), 6), ((2, 4), 8), ((2, 6), 12), ((2, 0), 0)])
    def test_calc_mul(self, input_args, expected):
        s = mul(*input_args)
        assert s == expected, "Multiplication failed"
