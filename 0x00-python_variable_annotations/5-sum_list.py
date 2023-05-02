#!/usr/bin/python3
"""
contains a function which takes a list input_list of floats
as argument and returns their sum as a float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ returns sum of the floats """
    a: float = 0
    for i in input_list:
        a += i

    return a
