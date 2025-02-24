#!/usr/bin/python3
"""Export all employees' tasks to a JSON file."""
import json
import requests


def export_all_to_json():
    """Export all employees' tasks to a JSON file."""
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"
    todos_url = f"{base_url}/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    if users_response.status_code != 200 or todos_response.status_code != 200:
        print("Failed to fetch data")
        return

    users_data = users_response.json()
    todos_data = todos_response.json()

    all_tasks = {}
    for user in users_data:
        user_id = user.get("id")
        username = user.get("username")
        user_tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos_data if task.get("userId") == user_id
        ]
        all_tasks[str(user_id)] = user_tasks

    json_filename = "todo_all_employees.json"
    with open(json_filename, mode='w') as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    export_all_to_json()