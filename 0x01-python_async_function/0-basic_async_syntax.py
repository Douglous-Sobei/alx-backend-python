#!/usr/bin/env python3

"""
    Basic syntax await async
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
        Args:
            max_delay: Max wait

        Return:
            Float time random
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
