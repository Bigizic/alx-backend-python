#!/usr/bin/env python3
"""a type-annotated function to_kv
@param (k): <str>
@param (v): <int> || <float>

Return: a tuple, first element of the stuple is string k and second
the square of the int/float v
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Implementation """
    return (k, v ** 2)
