#!/usr/bin/env python3
"""
Module to handle mixed types
"""

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function that find sum for a mixed list

    args:
        mxd_lst: list of integers and floats

    return: sum of all numbers
    """
    return float(sum(mxd_lst))
