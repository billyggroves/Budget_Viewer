from transaction_loader import load_transactions
from categories import CATEGORIES
from category import Category
from decimal import Decimal

def load_categories():
    cats = []
    sums = find_sums()
    for s in sums:
        print(f"{s}: {sums[s]}")
    for i,cat in enumerate(CATEGORIES):
        cats.append(Category(cat, i, sums))
    
    for cat in cats:
        print(f"Category: {cat}")
    return cats

def find_sums():
    sums = dict()
    transactions = load_transactions()
    for cat in CATEGORIES:
        sums[cat] = sum_category(transactions, cat)
    sums["Total Income"] = sums["Income"] + sums["Misc Income"]
    sums["Total Liabilities"] = sums["Mortgage/Rent"] + sums["Utilities"] + sums["Groceries"] + sums["Fuel"] + sums["Insurance"] + sums["Restaurants"] + sums["Shopping"] + sums["Subscriptions"] + sums["Misc"]
    sums["Profit"] = sums["Total Income"] - sums["Total Liabilities"]
    sums[""] = sums["Profit"]
    return sums
    
def sum_category(transactions, category):
    count = Decimal('0.00')
    # print(transactions[0])
    # print(f"Main Category: {category}")
    # if category in CATEGORIES[:2]:
    for transaction in transactions['debit']:
        if transaction.category == category:
            # print(f"Trans Cat:{transaction.category}")
            if category == "Misc":
                print(transaction)
            count += Decimal(str(transaction.amount))
    # if category in CATEGORIES[5:]:
    for transaction in transactions['credit']:
        if transaction.category == category:
            if category == "Misc":
                print(transaction)
            count += Decimal(str(transaction.amount))
    return count