from category_loader import load_categories
from diagram import build_diagram

"""
TODO:
    Add testing
    Edge cases
        Negative Profit
        Rethink handling of CC payments, count or ignore?
    Add more transaction label filtering
    Change Profit to Savings
    General cleanup and refactoring
    Sankey frontend, make it pretty :D
    Remove the blank node?
    Add lables to links?
"""

def main():
    categories = load_categories()
    build_diagram(categories)

if __name__ == "__main__":
    main()