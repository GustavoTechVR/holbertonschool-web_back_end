#!/usr/bin/env python3
"""
Module with a type-annotated function to_kv
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function that takes a string and an int/float and returns a tuple.

    Args:
        k (str): The input string.
        v (Union[int, float]): The input int or float.

    Returns:
        Tuple[str, float]: A tuple where the first element is the input string k,
                          and the second element is the square of the input int/float v.
    """
    return (k, v ** 2)
