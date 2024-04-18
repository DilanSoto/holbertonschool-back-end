#!/usr/bin/python3
"""
Given a specific API, returns information about the user's TODO list progress
"""
from sys import argv
import csv
import requests


if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(url)
    user = response.json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
    response = requests.get(url)
    todos = response.json()

    with open('{}.csv'.format(user_id), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([user_id, user.get("username"),
                             todo.get("completed"), todo.get("title")])
