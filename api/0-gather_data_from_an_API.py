#!/usr/bin/python3

"""
Write a Python script that, using this REST API, for a given employee ID
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    response = requests.get(url)
    user = response.json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(argv
                                                                        [1])
    response = requests.get(url)
    todos = response.json()
    completed = [todo.get("title") for todo in todos if todo.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(user.get("name"),
                                                          len(completed),
                                                          len(todos)))
    [print("\t {}".format(todo)) for todo in completed]
