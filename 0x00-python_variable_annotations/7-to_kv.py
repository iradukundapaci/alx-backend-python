#!/usr/bin/env python3
"""
Module that handle data
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function that turns parameter to tuple

    args:
        k: string
        v: integer or float

    return: created tuple
    """
    return (k, v ** 2)
