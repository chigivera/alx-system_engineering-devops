#!/usr/bin/python3
"""Export an employee's TODO list progress to a JSON file."""
import json
import requests
import sys


def export_to_json(employee_id):
    """Export the TODO list progress for a given employee ID to a JSON file."""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Failed to fetch data")
        return

    user_data = user_response.json()
    todos_data = todos_response.json()

    json_data = {
        str(employee_id): [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user_data.get("username")
            }
            for task in todos_data
        ]
    }

    json_filename = f"{employee_id}.json"
    with open(json_filename, mode='w') as json_file:
        json.dump(json_data, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_json(employee_id)