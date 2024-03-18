#!/usr/bin/env python3
"""
Python Async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Function that receives a delay integer for the sleep time

    args:
        max_delay: max delay time

    return: delay time
    """
    delay: float = random.uniform(0, float(max_delay))
    await asyncio.sleep(delay)
    return delay
