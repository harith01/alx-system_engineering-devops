#!/usr/bin/python3
"""Gather data from an API"""

import requests as re
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee = re.get("{}users/{}".format(url, sys.argv[1])).json()
    todos = re.get("{}todos?userId={}".format(url, sys.argv[1])).json()
    completed = [to_do for to_do in todos if to_do.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(employee.get('name'),
          len(completed), len(todos)))
    [print("\t {}".format(to_do.get('title'))) for to_do in completed]
