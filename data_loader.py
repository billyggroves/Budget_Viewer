import csv
import os
from transaction import Transaction

"""
    TODO
        - Create categorys, with rules and potentially create more branches in transactions{}
"""


def load():
    transactions = {}
    transactions['credit'] = []
    transactions['debit'] = []
    directory = "./data"
    for file in os.listdir(directory):
        with open(directory + '/' + file, mode='r') as file:
            reader = csv.reader(file)
            print(f"loading.... {file.name}")
            date = None
            t_type = None
            description = None
            amount = None
            debit = None
            credit = None
            for i, row in enumerate(reader):
                if i == 0:
                    if 'Date' in row:
                        date = row.index('Date')
                    if 'Transaction' in row:
                        t_type = row.index('Transaction')
                    if 'Description' in row:
                        description = row.index('Description')
                    if 'Name' in row:
                        description = row.index('Name')
                    if 'Amount' in row:
                        amount = row.index('Amount')
                    if 'Debit' in row:
                        debit = row.index('Debit')
                    if 'Credit' in row:
                        credit = row.index('Credit')
                    print(f"indexes: date: {date}, t_type: {t_type}, desc: {description}, amount: {amount}, debit: {debit}, credit: {credit}")
                    continue
                if date is not None and description is not None:
                    # TODO Find better way to achieve this, as it could cause issues
                    # potential fixes, if (name of CC company in ...)
                    if "payment" in row[description].lower():
                        continue
                    if (debit is None 
                    and credit is None 
                    and amount is not None):
                        if t_type is not None:
                            if row[t_type] == "DEBIT":
                                transactions['debit'].append(Transaction(row[date],row[description],float(row[amount])))
                            elif row[t_type] == "CREDIT":
                                transactions['credit'].append(Transaction(row[date],row[description],float(row[amount])))
                        else:
                            if float(row[amount]) > 0.0:
                                transactions['debit'].append(Transaction(row[date],row[description],float(row[amount])))
                            else:
                                transactions['credit'].append(Transaction(row[date],row[description],float(row[amount])))
                    elif debit is not None and credit is not None:
                        if row[credit] == '':
                            transactions['debit'].append(Transaction(row[date],row[description],float(row[debit])))
                        else:
                            transactions['credit'].append(Transaction(row[date],row[description],float(row[credit])))
                    else:
                        print(f"something is wrong with this transaction: {row}")
                else:
                    print(f"something is wrong with this transaction or CSV: {row}")
            print(f"{len(transactions['credit']) + len(transactions['debit'])} transactions loaded")
    for tran in transactions['credit']:
        print("Credit")
        print(tran)
    for tran in transactions['debit']:
        print("Debit")
        print(tran)
    return transactions
    

load()