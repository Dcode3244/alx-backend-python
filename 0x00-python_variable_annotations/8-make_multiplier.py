#!/usr/bin/env python3
"""
contains a function that takes a float multiplier as argument and
returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a function that multiplies a float by multiplier """
    def x(a: float) -> float:
        return multiplier * a

    return x
