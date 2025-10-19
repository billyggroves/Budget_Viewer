from category_loader import load_categories
from diagram import build_diagram

"""
TODO:
    Add testing
    Edge cases
        Rethink handling of CC payments, count or ignore?
    Add more transaction label filtering
    General cleanup and refactoring
    Add node alignment to keep from crossovers or overlaps
    Sankey frontend, make it pretty :D
"""

def main():
    categories = load_categories()
    build_diagram(categories)

if __name__ == "__main__":
    main()