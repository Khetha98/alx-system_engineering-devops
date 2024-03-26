#!/usr/bin/python3
"""to-do list information for the given employee ID."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]

    user_response = requests.get(
        url + "users/{}".format(employee_id)
    )
    todos_response = requests.get(
        url + "todos", params={"userId": employee_id}
    )

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Failed to fetch data. Please try again later.")
        sys.exit(1)

    user = user_response.json()
    todos = todos_response.json()

    completed_tasks = [task for task in todos if task.get('completed')]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed_tasks), len(todos)
    ))

    for task in completed_tasks:
        print("\t{}".format(task.get("title")))
