import csv
import os

"""
    TODO
        - Create categorys, with rules
        - update load() to
            - Check if row[1] in category
            - sum by category
"""


def load():
    labels = []
    amounts = []

    directory = "./data"
    for file in os.listdir(directory):
        with open(directory + '/' + file, mode='r') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    continue
                labels.append(row[1])
                amounts.append(float(row[2]))
    print(labels)
    print(amounts)

load()