#!/usr/bin/python3
""" returns information about his/her TODO list progress"""


if __name__ == "__main__":
    """change imports"""
    import requests
    from sys import argv

    employee_id = int(argv[1])
    base_url = f"https://jsonplaceholder.typicode.com/users/{id}"

    EMPLOYEE_NAME = requests.get(base_url).json()["name"]
    task_record = requests.get(base_url + "/todos").json()
    task_completed = [task for task in task_record if task["completed"]]

    print(f"Employee {EMPLOYEE_NAME} is done", end="")
    print(f" with tasks({len(task_completed)}/{len(task_record)}):")

    for task in task_completed:
        print(f"\t {task['title']}")
