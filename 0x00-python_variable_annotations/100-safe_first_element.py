#!/usr/bin/env python3
"""
Module to detect element type
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Function to retrieve first element

    args:
        lst: list of elements

    return: element or none
    """
    if lst:
        return lst[0]
    else:
        return None
