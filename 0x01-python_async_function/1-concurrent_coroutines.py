#!/usr/bin/env python3

"""
    Croutine at the same time with sync.
"""

from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
        Args:
            max_delay: Max wait
            n: Spawn function

        Return:
            Float time random
    """
    delays: List[float] = []
    tasks: List = []

    for _ in range(n):
        tasks.append(wait_random(max_delay))

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
