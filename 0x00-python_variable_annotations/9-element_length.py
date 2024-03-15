#!/usr/bin/env python3
"""
Module that hadles iterables
"""
from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function to find length of iterable

    args:
        lst: iterable

    return: length of iterable
    """
    return [(i, len(i)) for i in lst]
