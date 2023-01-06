#!/usr/bin/env python3
"""
Complex types - functions
Write typed-annotated function make_multiplier that takes float multiplier argument
Returns function that multiplies a float by a multipier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Typed-annotated function
    make_multiplier
    """

    def fn(num: float):
        """
        multiplier function
        """
        return num * multiplier
    return fn
