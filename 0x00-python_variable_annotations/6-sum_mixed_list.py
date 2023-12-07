#!/usr/bin/env python3
""" a type-annotated function sum_mixed_list()
@param (mxd_lst): <list of integers>

Return: sum of argument as float
"""

from typing import List


def sum_mixed_list(mxd_list: List[int]) -> float:
    """ Implementation """
    return sum(mxd_list)
