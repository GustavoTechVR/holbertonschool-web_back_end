#!/usr/bin/env python3
"""
Module with measure_time function
"""

from typing import Callable
import time

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns total_time / n
    Args:
        n (int): Number of times to spawn wait_random
        max_delay (int): Maximum delay for wait_random
    Returns:
        float: Total execution time divided by n
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n

# Example usage
if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
