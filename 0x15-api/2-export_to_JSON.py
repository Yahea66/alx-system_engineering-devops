#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import csv
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url_user = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    url_tasks = "https://jsonplaceholder.typicode.com/todos"
    params = {"userId": user_id}
    user = requests.get(url_user).json()
    name = user.get("username")
    tasks = requests.get(url_tasks, params=params).json()

    dic = {}
    lis = []
    for task in tasks:
        inner = {"task": task.get("title"),
                 "completed": task.get("completed"),
                 "username": name}
        lis.append(inner)
    dic[str(user_id)] = lis

    file_name = f"{user_id}.json"
    with open(file_name, mode='w') as f:
        json.dump(dic, f)
