#!/usr/bin/env python3
"""Annotate the below function’s parameters and return values with the
appropriate types"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing the length of each element and the
    element itself"""
    return [(i, len(i)) for i in lst]
