#!/usr/bin/env python3
"""
Async Comprehensions
Write coroutine async_comprehension, takes no arguments
Return 10 random numbers collected using async comprehensions
"""
from typing import List
Vector = List[float]

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Vector:
    """
    Coroutine async_comprehension
    yield random numbers collected
    """
    stop = [y async for y in async_generator()]
    return stop
