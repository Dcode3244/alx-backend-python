#!/usr/bin/env python3
"""
contains a function which takes a list mxd_lst of integers
and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ returns sum of the numbers in the list as a float """
    a: float = 0
    for i in mxd_list:
        a += i

    return a
