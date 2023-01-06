#!/usr/bin/env python3
"""
Complex types - mixed list
Write typed-annotated function sum_mixed_list
takes mxd_lst integers and floats
Returns their sum as float
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Typed-annotated function
    sum_mixed_list
    """
    return sum(mxd_lst)
