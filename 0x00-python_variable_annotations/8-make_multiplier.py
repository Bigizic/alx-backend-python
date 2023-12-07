#!/usr/bin/env python3
"""a type-annotated function make_multiplier()
@param (multiplier): <float>

Return: function that multiplies a float by multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Implementation """
    def fun_multiplier(num: float) -> float:
        """ multiplies a float """
        return num * multiplier
    return fun_multiplier
