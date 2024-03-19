#!/usr/bin/env python3
"""
PYTHON ASYNC MODULE
"""
import asyncio
from typing import AsyncGenerator
import random


async def async_generator() -> AsyncGenerator[float, float]:
    """
    Function that creates async generator

    return: async generator
    """
    for _ in range(10):
        await asyncio.sleep(1)
        random_number = random.uniform(0, 10)
        yield random_number
