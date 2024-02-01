#!/usr/bin/env python3
"""
Module with a type-annotated function make_multiplier
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that takes a float multiplier and returns a function.

    Args:
        multiplier (float): The input float multiplier.

    Returns:
        Callable[[float], float]: A function that takes a float and multiplies it by the multiplier.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
