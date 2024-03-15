#!/usr/bin/env python3
"""
Module to handle lists
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Function that calculates sum of number in a list of floats

    args:
        input_list: list of floats

    return: sum of all float in the list
    """
    return float(sum(input_list))
