#!/usr/bin/env python3
""" Measures the total execution time for wait_n
@param (n): <int>
@param (max_delay): <int>

Return: total_time / n <float>
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Implementation """
    s_time = time.perf_counter()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.perf_counter()

    return (end_time - s_time) / n
