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

if __name__ == "__main__":
    # Retrieve the employee ID from the command line arguments.
    employee_id = int(sys.argv[1])

    # Construct the URL to fetch the employee's information.
    employee_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        employee_id)

    # Send a GET request to the employee URL and convert the response to JSON.
    user_response = requests.get(employee_url)
    user_info = user_response.json()

    # Extract the employee's name from the JSON response.
    EMPLOYEE_NAME = user_info.get('name')

    # Construct the URL to fetch the employee's tasks.
    alltasks_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        employee_id)

    # Send a GET request to the tasks URL and convert the response to JSON.
    alltasks_response = requests.get(alltasks_url)
    todos = alltasks_response.json()

    # Calculate the total number of tasks and the number of completed tasks.
    TOTAL_NUMBER_OF_TASKS = len(todos)
    done_tasks = [task for task in todos if task.get('completed') is True]
    NUMBER_OF_DONE_TASKS = len(done_tasks)

    # Print the employee's progress.
    print('Employee {} is done with tasks({}/{}):'.format(EMPLOYEE_NAME,
          NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

    # Print the title of each completed task.
    for task in done_tasks:
        print('\t {}'.format(task.get('title')))
