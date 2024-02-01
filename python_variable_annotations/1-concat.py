#!/usr/bin/env python3
"""
Module with a type-annotated function concat
"""

def concat(str1: str, str2: str) -> str:
    """
    Function that takes two strings and returns their concatenation.

    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        str: The concatenated string.
    """
    return str1 + str2
