#!/usr/bin/env python3
"""
contains code with correct duck-typed annotations
"""
from typing import Sequence, Union, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ correct duck-typed annotations """
    if lst:
        return lst[0]
    else:
        return None
