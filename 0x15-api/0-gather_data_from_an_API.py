#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url_user = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    url_tasks = "https://jsonplaceholder.typicode.com/todos"
    params = {"userId": user_id}
    user = requests.get(url_user).json()
    name = user.get("name")
    tasks = requests.get(url_tasks, params=params).json()
    total_tasks = len(tasks)
    completed = sum(1 for task in tasks if task.get("completed"))
    print(f"Employee {name} is done with tasks({completed}/{total_tasks}):")

    completed_tasks = [task.get("title") for task in tasks
                       if task.get("completed")]
    for task in completed_tasks:
        print(f"\t {task}")
