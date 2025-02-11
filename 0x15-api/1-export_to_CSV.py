#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import csv
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

    file_name = f"{user_id}.csv"
    with open(file_name, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([user_id, name, str(task.get("completed")),
                             task.get("title")])
