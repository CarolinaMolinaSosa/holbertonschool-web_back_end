#!/usr/bin/env python3
"""Task 2: Measure Asynchronous Comprehension Runtime"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """Measure the total runtime of multiple async_comprehension calls and return it."""
    start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    end_time = time.time()
    total_runtime = end_time - start_time
    return total_runtime
