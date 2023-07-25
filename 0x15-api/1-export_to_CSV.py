#!/usr/bin/python3
"""Gather data from an API"""

import requests as re
import sys
import csv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee = re.get("{}users/{}".format(url, sys.argv[1])).json()
    todos = re.get("{}todos?userId={}".format(url, sys.argv[1])).json()
    completed = [to_do for to_do in todos if to_do.get('completed') is True]
    data = []
    for to_do in todos:
        row = [employee.get('id'), employee.get('username'),
               to_do.get('completed'), to_do.get('title')]
        data.append(row)
    with open('USER_ID.csv', 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(data)
