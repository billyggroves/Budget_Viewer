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
    transactions = []
    directory = "./data"
    for file in os.listdir(directory):
        with open(directory + '/' + file, mode='r') as file:
            reader = csv.reader(file)
            description = 0
            debit = 0
            credit = 0
            for i, row in enumerate(reader):
                if i == 0:
                    description = row.index('Description')
                    if 'Amount' in row:
                        debit = row.index('Amount')
                    if 'Debit' in row:
                        debit = row.index('Debit')
                    if 'Credit' in row:
                        credit = row.index('Credit')
                    # print(f"indexes: {description}, {debit}, {credit}")
                    continue
                if row[debit] == '':
                    transaction = (row[description],0.00,float(row[credit]))
                elif float(row[debit]) < 0:
                    transaction = (row[description],0.00,float(row[debit]))
                else:
                    transaction = (row[description],float(row[debit]),0.00)
                transactions.append(transaction)
    return transactions
    

load()