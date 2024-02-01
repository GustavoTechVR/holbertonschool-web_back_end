#!/usr/bin/env python3
"""
Module with a type-annotated function floor
"""

import math

def floor(n: float) -> int:
    """
    Function that takes a float and returns its floor.

    Args:
        n (float): The input float.

    Returns:
        int: The floor of the input float.
    """
    return math.floor(n)
