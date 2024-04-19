#!/usr/bin/python3
"""
File: 1-export_to_CSV.py
Author: TheWatcher01
Date: 2024-04-15
Description: This script fetches an employee's TODO tasks from a REST API
and exports the data into a CSV file.
"""

import csv
import requests
import sys

if __name__ == '__main__':
    # Convert the first command line argument to an integer to use as the
    # employee ID.
    employee_id = int(sys.argv[1])

    # Construct the URL to fetch the employee's information.
    base_url = 'https://jsonplaceholder.typicode.com/users/'
    employee_url = '{}{}'.format(base_url, employee_id)

    # Send a GET request to the employee URL and convert the response to JSON.
    user_response = requests.get(employee_url)
    user_info = user_response.json()

    # Extract the employee's username from the JSON response.
    EMPLOYEE_NAME = user_info.get('username')

    # Construct the URL to fetch all tasks assigned to the employee.
    tasks_url = '{}{}/todos'.format(base_url, employee_id)

    # Send a GET request to the tasks URL and convert the response to JSON.
    tasks_response = requests.get(tasks_url)
    todos = tasks_response.json()

    # Create a list of all tasks, each represented as a list of four elements:
    # user ID, username, task completion status, and task title.
    all_tasks = []
    for task in todos:
        task_data = [task.get('userId'), EMPLOYEE_NAME,
                     task.get('completed'), task.get('title')]
        all_tasks.append(task_data)

    # Write the list of all tasks into a CSV file, with each task as a row.
    with open('{}.csv'.format(employee_id), 'w', newline='',
              encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(all_tasks)
