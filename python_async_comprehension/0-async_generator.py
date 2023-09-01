#!/usr/bin/env python3
"""Task 0: Asynchronous Generator"""

import asyncio
from random import uniform
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """Generate 10 random floating-point numbers with a 1-second delay between each."""
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
