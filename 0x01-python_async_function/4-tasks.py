#!/usr/bin/env python3
""" alters a function
"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Implementation """
    spawns = [task_wait_random(max_delay) for _ in range(n)]
    # task = [asyncio.create_task(x) for x in spawns]

    result = await asyncio.gather(*spawns)
    new_list = []
    while result:
        min_e = min(result)
        new_list.append(min_e)
        result.remove(min_e)

    return new_list
