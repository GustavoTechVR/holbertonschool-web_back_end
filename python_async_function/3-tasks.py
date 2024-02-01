#!/usr/bin/env python3
"""
Module with task_wait_random function
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Function that takes an integer max_delay and returns an asyncio.Task
    Args:
        max_delay (int): Maximum delay for wait_random
    Returns:
        asyncio.Task: Task for wait_random coroutine
    """
    return asyncio.create_task(wait_random(max_delay))

# Example usage
if __name__ == "__main__":
    async def test(max_delay: int) -> float:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
