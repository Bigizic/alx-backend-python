#!/usr/bin/env python3
"""An Async Generator

Return: random number 10 times!!
"""

import asyncio
import random


async def async_generator():
    """ Implementation """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
