#!/usr/bin/env python3
"""
Tasks
Alter a code into a new function task_wait_n
"""
import asyncio
from typing import List

get = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function task_wait_n
    Alter code
    """
    ls = [get(max_delay) for i in range(n)]
    stop = [await task for task in asyncio.as_completed(ls)]
    return stop
