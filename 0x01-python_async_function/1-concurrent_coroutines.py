#!/usr/bin/env python3
""" async routine that spawns
@param (n): <int>
@param (max_delay): <int>

Return: list of all the delays <float> values
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """ Implementation """
    spawns = [wait_random(max_delay) for _ in range(n)]
    task = [asyncio.create_task(x) for x in spawns]

    result = await asyncio.gather(*task)

    return result
