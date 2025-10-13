class Transaction:
    def  __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = abs(amount)

    def __repr__(self):
        return f"Transaction: {self.date}, {self.category}, {self.description}, ${self.amount}"