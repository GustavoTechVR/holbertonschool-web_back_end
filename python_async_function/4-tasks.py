#!/usr/bin/env python3
"""
Module with task_wait_n function
"""

from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous function that spawns task_wait_random n times with the specified max_delay
    Args:
        n (int): Number of times to spawn task_wait_random
        max_delay (int): Maximum delay for task_wait_random
    Returns:
        List[float]: List of delays in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return await asyncio.gather(*tasks)

# Example usage
if __name__ == "__main__":
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
