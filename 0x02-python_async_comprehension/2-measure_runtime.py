#!/usr/bin/env python3
"""
Runtime for parallel comprehensions
Write coroutine measure_runtime to execute async_comprehension
measure_runtime to measure total runtime and return it
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine measure_runtime
    measure execute runtime
    """
    begin = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    stop = time.perf_counter()
    return stop - begin
