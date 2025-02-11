#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import csv
import json
import requests

if __name__ == "__main__":
    url_user = "https://jsonplaceholder.typicode.com/users"
    url_tasks = "https://jsonplaceholder.typicode.com/todos"
    users = requests.get(url_user).json()

    dic = {}
    for user in users:
        lis = []
        user_id = user.get("userId")
        params = {"userId": user_id}
        tasks = requests.get(url_tasks, params=params).json()
        for task in tasks:
            inner = {"username": user.get("username"),
                     "task": task.get("title"),
                     "completed": task.get("completed")}
            lis.append(inner)
        dic[str(user_id)] = lis

    file_name = "todo_all_employees.json"
    with open(file_name, mode='w') as f:
        json.dump(dic, f)
