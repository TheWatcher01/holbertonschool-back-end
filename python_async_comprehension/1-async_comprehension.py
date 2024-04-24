#!/usr/bin/env python3

"""
Module: 2-main.py
Author: TheWatcher01
Date: 2024-04-24
Description: This module imports & utilizes measure_runtime function
from the 2-measure_runtime module. It prints result of the function.
"""

import asyncio

# Importing measure_runtime function from the 2-measure_runtime module
measure_runtime = __import__('2-measure_runtime').measure_runtime


async def main():
    """
    Asynchronous function that returns result of measure_runtime function.

    This function awaits result of measure_runtime function and returns it.
    """
    return await measure_runtime()  # Return result of measure_runtime function

# Run the main function using asyncio.run function and print result
print(asyncio.run(main()))
