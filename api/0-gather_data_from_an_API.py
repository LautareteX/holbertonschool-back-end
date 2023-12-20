#!/usr/bin/python3
""" returns information about his/her TODO list progress"""
import requests
from sys import argv


if __name__ == "__main__":
    employee_id = argv[1]
    complete_tasks = 0
    total = 0
    complete_list = []

    employee = (requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"))
    employee_todos = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")

    for i in employee_todos.json():
        if i['completed']:
            complete_tasks += 1
            complete_list.append(i)
        total += 1

    print(f"Employee {employee.json()['name']} "
          f"is done with tasks({complete_tasks}/{total}):")
    for task in complete_list:
        print(f"\t {task['title']}")
