#!/usr/bin/python3
"""
Given a specific API, returns information about the user's TODO list progress
"""
from sys import argv
import json
import requests

if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(url)
    user = response.json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)
    response = requests.get(url)
    todos = response.json()

    tasks = []
    for todo in todos:
        task_dict = {"task": todo.get("title"),
                     "completed": todo.get("completed"),
                     "username": user.get("username")}
        tasks.append(task_dict)

    with open('{}.json'.format(user_id), 'w') as file:
        json.dump({user_id: tasks}, file)
