#!/usr/bin/env python
"""A coroutine that collects 10 random numbers using async comprehensing

Return: 10 random number from async_generator
"""

import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """ Implementation """
    return [number async for number in async_generator()]
