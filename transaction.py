from enum import Enum

class Transaction_Type(Enum):
    DEBIT = "DEBIT"
    CREDIT = "CREDIT"


class Transaction:
    def  __init__(self, description, transaction_type, amount):
        self.description = description
        self.transaction_type = transaction_type
        self.amount = abs(amount)

    def __repr__(self):
        return f"Transaction: {self.description}, {self.transaction_type}, ${self.amount}"