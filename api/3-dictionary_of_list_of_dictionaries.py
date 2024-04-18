#!/usr/bin/python3
"""
Given a specific API, returns information about all users' TODO
list progress
"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()

    all_tasks = {}

    for user in users:
        user_id = user.get("id")
        url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            user_id)
        response = requests.get(url)
        todos = response.json()

        tasks = []
        for todo in todos:
            task_dict = {"username": user.get("username"),
                         "task": todo.get("title"),
                         "completed": todo.get("completed")}
            tasks.append(task_dict)

        all_tasks[user_id] = tasks

    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_tasks, file)
