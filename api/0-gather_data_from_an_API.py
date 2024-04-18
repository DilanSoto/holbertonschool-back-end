#!/usr/bin/python3
"""
Script to retrieve and display information about an employee's TODO list progress
"""
import sys
import requests

def get_employee_todo_progress(employee_id):
    """
    Retrieve and display the employee's TODO list progress
    """
    # URL of the REST API
    todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)

    try:
        # Send GET request to the API
        todos_response = requests.get(todos_url)
        user_response = requests.get(user_url)
        todos_response.raise_for_status()  # Raise exception for bad status codes
        user_response.raise_for_status()  # Raise exception for bad status codes

        # Parse JSON response
        todos = todos_response.json()
        user = user_response.json()

        # Extract employee name
        employee_name = user['name']

        # Count completed tasks
        completed_tasks = [todo for todo in todos if todo['completed']]
        num_completed_tasks = len(completed_tasks)
        total_tasks = len(todos)

        # Print employee TODO list progress
        print("Employee {} is done with tasks({}/{}):".format(employee_name, num_completed_tasks, total_tasks))
        for todo in completed_tasks:
            print("\t {}".format(todo['title']))

    except requests.exceptions.HTTPError as errh:
        print ("HTTP Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc) 
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
    except requests.exceptions.RequestException as err:
        print ("Something Else:",err)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: {} <employee_id>'.format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)