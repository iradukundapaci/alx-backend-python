#!/usr/bin/env python3
"""
PYTHON ASYNC MODULE
"""
import time
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Function that querry async generator

    return: float
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    stop_time = time.perf_counter() - start_time

    return stop_time
