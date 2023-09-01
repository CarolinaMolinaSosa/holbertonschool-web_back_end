#!/usr/bin/env python3
"""Task 2"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(num_calls: int, max_delay: int) -> float:
    """
    Measure the total execution time
    """
    start_time = time.time()
    asyncio.run(wait_n(num_calls, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / num_calls
