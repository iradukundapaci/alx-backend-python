#!/usr/bin/env python3
"""
Module that handles multiplication
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that handles multpication of base number

    args:
        multiplier: base number

    return: function to do multiplication
    """
    inside_fun: callable[[float], float] = lambda x: multiplier * x
    return inside_fun
