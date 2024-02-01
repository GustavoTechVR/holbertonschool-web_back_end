#!/usr/bin/env python3
"""
Module with type-annotated function safely_get_value
"""

from typing import Mapping, Any, TypeVar, Union, Optional

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Optional[T] = None) -> Union[Any, T]:
    """
    Function that safely gets a value from a dictionary based on the key.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to look up in the dictionary.
        default (Optional[T]): The default value to return if the key is not found (default is None).

    Returns:
        Union[Any, T]: The value associated with the key if it exists, otherwise, the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
