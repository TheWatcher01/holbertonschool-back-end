#!/usr/bin/python3
"""Exporting an employee's data into a json file"""

import json
import requests
import sys


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    # Get the employee's name
    employee_url = ("https://jsonplaceholder.typicode.com/users/"
                    f"{employee_id}")
    # Converts the response from the server into a Python dictionary
    user_response = requests.get(employee_url)
    user_info = user_response.json()
    EMPLOYEE_NAME = user_info.get('username')

    # Get all the tasks of an employee
    alltasks_url = ("https://jsonplaceholder.typicode.com/users/"
                    f"{employee_id}/todos")
    alltasks_response = requests.get(alltasks_url)
    todos = alltasks_response.json()

    # Converting the data into a dictionary
    all_tasks = []
    for task in todos:
        dict = {'task': task.get('title'), 'completed': task.get('completed'),
                'username': EMPLOYEE_NAME}
        all_tasks.append(dict)
    tasks_dict = {task.get('userId'): all_tasks}

    # Converting the data into a json file
    with open(f"{employee_id}.json", 'w', encoding='utf8') as f:
        json_list = json.dump(tasks_dict, f)
