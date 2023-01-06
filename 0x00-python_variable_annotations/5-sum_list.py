#!/usr/bin/env python3
"""
Complex types - list of floats
Write type-annotated function sum_list, takes input_list of floats
as arguments
Returns their sum as float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Typed-annotated function
    sum_list
    """
    return sum(input_list)
