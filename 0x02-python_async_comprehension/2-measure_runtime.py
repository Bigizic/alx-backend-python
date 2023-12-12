#!/usr/bin/env python3
"""A coroutine that execute async_comprehension() four times in parallel
using asyncio.gather
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """ Implementation """
    s_time = time.perf_counter()
    spawns = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*spawns)
    end_time = time.perf_counter()

    return end_time - s_time
