#!/usr/bin/env python3
"""Import async_comprehension from the previous file
and write a measure_runtime coroutine that will execute
async_comprehension four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it
to yourself."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """async_comprehension: collect 10 random numbers using an async
    comprehensing over async_generator, then return the 10 random numbers."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


