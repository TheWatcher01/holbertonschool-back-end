#!/usr/bin/python3
"""
File: 3-dictionary_of_list_of_dictionaries.py
Author: TheWatcher01
Date: 2024-04-15
Description: This script fetches TODO tasks of all employees from a REST API
and exports the data into a JSON file.
"""

import json
import requests

if __name__ == '__main__':
    # Construct the URL to fetch all employees' information.
    base_url = 'https://jsonplaceholder.typicode.com/users/'

    # Send a GET request to employees URL and convert response to JSON.
    employees_response = requests.get(base_url)
    employees = employees_response.json()

    # Initialize an empty dictionary to store tasks data.
    tasks_dict = {}

    # Loop over all employees.
    for employee in employees:
        # Construct URL to fetch all tasks assigned to current employee.
        tasks_url = '{}{}/todos'.format(base_url, employee['id'])

        # Send a GET request to the tasks URL and convert the response to JSON.
        tasks_response = requests.get(tasks_url)
        todos = tasks_response.json()

        # Create list of all tasks, each represented as dictionary with keys
        # 'username', 'task', and 'completed'.
        all_tasks = []
        for task in todos:
            task_dict = {'username': employee['username'],
                         'task': task['title'], 'completed': task['completed']}
            all_tasks.append(task_dict)

        # Add list of tasks to tasks dictionary, using the employee's ID
        # as the key.
        tasks_dict[employee['id']] = all_tasks

    # Write the tasks dictionary into a JSON file.
    with open('todo_all_employees.json', 'w', encoding='utf-8') as f:
        json.dump(tasks_dict, f)
