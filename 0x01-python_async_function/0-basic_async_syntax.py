#!/usr/bin/env python3
"""an asynchronous coroutine
@param (max_delay): <int> 'default 10'

Return: max_delay
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Implementation """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
