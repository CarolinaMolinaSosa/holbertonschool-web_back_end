#!/usr/bin/env python3
"""Task 1"""


import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
