#!/usr/bin/python3
"""Gather data from an API"""

import json
import requests as re

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = re.get("{}users".format(url)).json()
    todos = re.get("{}todos".format(url)).json()
    my_dict = {}
    for user in users:
        todos_list = []
        todo_dict = {}
        for todo in todos:
            if user.get('id') == todo.get('userId'):
                todo_dict['task'] = todo.get('title')
                todo_dict['completed'] = todo.get('completed')
                todo_dict['username'] = user.get('username')
                todos_list.append(todo_dict)
        my_dict['{}'.format(user.get('id'))] = todos_list
    json_object = json.dumps(my_dict)
    with open('todo_all_employees.json', 'w') as f:
        f.write(json_object)
