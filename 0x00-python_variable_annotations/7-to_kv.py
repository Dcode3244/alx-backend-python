#!/usr/bin/env python3
"""
contains a functions that takes a string and an int or float as
arguments and returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ returns a tuple """
    x: float = v ** 2
    return (k, x)
