#!/usr/bin/env python3
""" annotation
"""

from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ implementation """
    return [(i, len(i)) for i in lst]
