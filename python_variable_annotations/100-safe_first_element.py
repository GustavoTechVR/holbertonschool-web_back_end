#!/usr/bin/env python3
"""
Module with duck-typed annotations for safe_first_element function
"""

from typing import Sequence, Optional, Any

def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Function that takes a sequence and returns its first element safely.

    Args:
        lst (Sequence[Any]): The input sequence.

    Returns:
        Optional[Any]: The first element of the sequence if it exists, otherwise, None.
    """
    if lst:
        return lst[0]
    else:
        return None
