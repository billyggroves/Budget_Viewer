import csv
import os
from transaction import Transaction, Transaction_Type

"""
    TODO
        - Create categorys, with rules
        - Fix bug with Negative transactions in Checking vs CC payments
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
                    if 'Transaction' in row:
                        transaction_type = row.index('Transaction')
                    if 'Description' in row:
                        description = row.index('Description')
                    elif 'Name' in row:
                        description = row.index('Name')
                    if 'Amount' in row:
                        debit = row.index('Amount')
                    if 'Debit' in row:
                        debit = row.index('Debit')
                    if 'Credit' in row:
                        credit = row.index('Credit')
                    # print(f"indexes: {description}, {debit}, {credit}")
                    continue
                if row[debit] == '':
                    transaction = Transaction(row[description],Transaction_Type.CREDIT,abs(float(row[credit])))
                elif float(row[debit]) < 0 or (transaction_type and transaction_type == "CREDIT"):
                    transaction = Transaction(row[description],Transaction_Type.CREDIT,abs(float(row[debit])))
                else:
                    transaction = Transaction(row[description],Transaction_Type.DEBIT,abs(float(row[debit])))
                transactions.append(transaction)
    for tran in transactions:
        print(tran)
    return transactions
    

load()