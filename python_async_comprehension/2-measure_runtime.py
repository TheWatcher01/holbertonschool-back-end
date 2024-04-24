#!/usr/bin/env python3

"""
File: 2-measure_runtime.py
Author: TheWatcher01
Date: 2024-04-24
Description: 
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    Asynchronous function that measures runtime of async_comprehension function

    This function measures the runtime of the async_comprehension function
    and returns the time it took to execute.
    """
    start_time = time.time()  # Start time of function execution
    tasks = [async_comprehension() for _ in range(4)]  # List of tasks to run
    await asyncio.gather(*tasks)  # Run all tasks concurrently
    end_time = time.time()  # End time of function execution
    return end_time - start_time  # Return time taken to execute function
