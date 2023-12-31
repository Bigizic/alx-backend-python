#!/usr/bin/env python3
""" async routine that spawns
@param (n): <int>
@param (max_delay): <int>

Return: list of all the delays <float> values
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Implementation """
    spawns = [wait_random(max_delay) for _ in range(n)]
    # task = [asyncio.create_task(x) for x in spawns]

    result = await asyncio.gather(*spawns)
    new_list = []
    while result:
        min_e = min(result)
        new_list.append(min_e)
        result.remove(min_e)

    return new_list
