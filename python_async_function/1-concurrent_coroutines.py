#!/usr/bin/env python3
"""
Module with asynchronous routine wait_n
"""

from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times with the specified max_delay
    Args:
        n (int): Number of times to spawn wait_random
        max_delay (int): Maximum delay for wait_random
    Returns:
        List[float]: List of delays in ascending order
    """
    delays = []

    async def wait_and_append_delay():
        delay = await wait_random(max_delay)
        delays.append(delay)

    await asyncio.gather(*(wait_and_append_delay() for _ in range(n)))

    return sorted(delays)

# Example usage
if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
