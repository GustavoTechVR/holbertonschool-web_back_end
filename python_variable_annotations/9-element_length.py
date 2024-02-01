#!/usr/bin/env python3
"""
Module with a type-annotated function element_length
"""

from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function that takes an iterable of sequences and returns a list of tuples.

    Args:
        lst (Iterable[Sequence]): The input iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where the first element is a sequence
                                    from the input and the second element is its length.
    """
    return [(i, len(i)) for i in lst]
