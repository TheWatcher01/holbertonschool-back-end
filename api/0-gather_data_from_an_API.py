#!/usr/bin/python3
"""
File: 0-gather_data_from_an_API.py
Author: TheWatcher01
Date: 2024-04-15
Description: This script fetches and displays the progress of a specific
employee's TODO tasks using a REST API.
"""

import requests
import sys


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    # Get the employee's name
    employee_url = ("https://jsonplaceholder.typicode.com/users/"
                    f"{employee_id}")
    user_response = requests.get(employee_url)
    user_info = user_response.json()
    EMPLOYEE_NAME = user_info.get('name')

    # Get all the tasks of an employee
    alltasks_url = ("https://jsonplaceholder.typicode.com/users/"
                    f"{employee_id}/todos")
    alltasks_response = requests.get(alltasks_url)
    todos = alltasks_response.json()

    # Count the total number of completed tasks and total tasks
    TOTAL_NUMBER_OF_TASKS = len(todos)
    count = 0
    for task in todos:
        if task.get('completed') is True:
            count += 1
    NUMBER_OF_DONE_TASKS = count

    print(
        f"Employee {EMPLOYEE_NAME} is done with tasks"
        f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

    # Print the title of completed tasks
    for task in todos:
        if task.get('completed') is True:
            print(f"\t {task.get('title')}")
