#!/usr/bin/python3
"""Fetch and display an employee's TODO list progress."""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Fetch and display the TODO list progress for a given employee ID."""
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

    employee_name = user_data.get("name")
    total_tasks = len(todos_data)
    done_tasks = sum(1 for task in todos_data if task.get("completed"))

    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for task in todos_data:
        if task.get("completed"):
            print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)