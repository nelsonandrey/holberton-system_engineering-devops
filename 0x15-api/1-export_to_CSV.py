#!/usr/bin/python3
"""export data in the CSV format."""

if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    ID = int(argv[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(ID)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(ID)).json()
    with open("{}.csv".format(ID), 'w') as csvf:
        filler = csv.writer(csvf, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in todo:
            filler.writerow([ID, user.get('username'),
                            task.get('completed'), task.get('title')])
