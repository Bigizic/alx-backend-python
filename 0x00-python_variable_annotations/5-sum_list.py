#!/usr/bin/env python3
"""a type-annotated function sum_list()
@param (input_list): <list of floats>

Return: sum of elements inside the list as a float
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Implementation """
    return sum(input_list)
