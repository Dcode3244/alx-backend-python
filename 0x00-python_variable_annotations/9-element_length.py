#!/usr/bin/env python3
"""
contains a function that returns list of tuple with
their length
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ returns values with appropriate types """
    return [(i, len(i)) for i in lst]
