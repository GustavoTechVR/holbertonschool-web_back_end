#!/usr/bin/env python3
"""
Async Generator Module
"""

import asyncio
import random

async def async_generator() -> float:
    """
    Coroutine that yields a random number between 0 and 10
    after asynchronously waiting for 1 second. Repeats this process 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

# Example of usage
# async def print_yielded_values():
#     result = []
#     async for i in async_generator():
#         result.append(i)
#     print(result)

# asyncio.run(print_yielded_values())
