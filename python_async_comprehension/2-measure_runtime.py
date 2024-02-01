#!/usr/bin/env python3
"""
Measure Runtime Module
"""

import asyncio
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel using asyncio.gather,
    measures the total runtime, and returns it.
    """
    start_time = asyncio.get_event_loop().time()

    # Execute async_comprehension four times in parallel
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = asyncio.get_event_loop().time()

    return end_time - start_time

# Example of usage
# async def main():
#     return await measure_runtime()

# print(asyncio.run(main()))
