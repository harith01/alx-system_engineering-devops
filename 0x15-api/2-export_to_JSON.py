#!/usr/bin/python3
"""Gather data from an API"""

import json
import requests as re
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee = re.get("{}users/{}".format(url, sys.argv[1])).json()
    todos = re.get("{}todos?userId={}".format(url, sys.argv[1])).json()
    completed = [to_do for to_do in todos if to_do.get('completed') is True]

    todos_list = []
    for todo in todos:
        todo_dict = {}
        todo_dict['task'] = todo.get('title')
        todo_dict['completed'] = todo.get('completed')
        todo_dict['username'] = employee.get('username')
        todos_list.append(todo_dict)
    my_dict = {'{}'.format(employee.get('id')): todos_list}
    json_object = json.dumps(my_dict)
    with open('{}.json'.format(employee.get('id')), 'w') as f:
        f.write(json_object)
