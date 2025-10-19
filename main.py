from category_loader import load_categories
from diagram import build_diagram

def main():
    categories = load_categories()
    build_diagram(categories)

if __name__ == "__main__":
    main()