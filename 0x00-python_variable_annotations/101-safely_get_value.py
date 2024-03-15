#!/usr/bin/env python3
"""
Module to detect element type
"""
from typing import Mapping, Any, Union, Optional, TypeVar

T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Optional[Union[T, None]] = None
) -> Union[Any, T]:
    """
    Function to get value in dictionaly

    args:
        dct: dictionaly
        key: dictionaly key
        default: default value

    return: dictional value or default value
    """
    if key in dct:
        return dct[key]
    else:
        return default
