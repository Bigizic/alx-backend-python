#!/usr/bin/env python3
"""a function that returns an asyncio.task
@param (max_delay): <int>

Return: asyncio.Task
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay):
    """ Implementation """
    return asyncio.create_task(wait_random(max_delay))
