class Transaction:
    def  __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = abs(amount)

    def __repr__(self):
        return f"Transaction: {self.date}, {self.description}, ${self.amount}"