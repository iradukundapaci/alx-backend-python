#!/usr/bin/env python3
"""
Python Async
"""
import time
from asyncio import run


wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Function to measure the execution time

    args:
        n: number of iterations
        max_delay: max time of delay

    return: time spent
    """
    start_time: time = time.perf_counter()
    run(wait_n(n, max_delay))
    stop_time: time = time.perf_counter() - start_time
    return stop_time
