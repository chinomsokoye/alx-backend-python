#!/usr/bin/env python3
"""
Duck type iterable object
Annotate a function param and return values
with appropriate types
"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotate function param
    element_length
    """
    return [(i, len(i)) for i in lst]
