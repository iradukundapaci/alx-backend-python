#!/usr/bin/env python3
"""
Python Async
"""
from asyncio import gather
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function to call wait_random for a given number of times

    args:
        n: number of iterations
        max_delay: maximun delay amount

    return: list of delays
    """
    functionCalls: List[callable[[int], float]] = [
        task_wait_random(max_delay) for _ in range(n)
    ]
    result: List[float] = await gather(*functionCalls)
    return sorted(result)
