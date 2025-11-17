# Budget Viewer - Agent Guidelines

## Build/Test Commands
- **Run application**: `python main.py`
- **Install dependencies**: `pip install -e .` or `uv sync`
- **Testing**: No test framework configured yet (TODO: Add pytest)
- **Linting**: No linter configured (TODO: Add ruff/black)

## Code Style Guidelines

### Imports & Structure
- Use standard Python import order: stdlib → third-party → local imports
- Import specific modules, not entire packages when possible
- Use relative imports for local modules (e.g., `from categories import CATEGORIES`)

### Naming Conventions
- Classes: PascalCase (e.g., `Category`, `Transaction`)
- Functions/variables: snake_case (e.g., `load_categories`, `node_colors`)
- Constants: UPPER_SNAKE_CASE (e.g., `CATEGORIES`, `INCOME`)
- Private methods: prefix with underscore (e.g., `_helper_method`)

### Type Handling
- Use `Decimal` for financial calculations to avoid floating point precision issues
- Convert amounts to absolute values with `abs()` for consistency
- Use `float()` only when interfacing with external libraries like Plotly

### Error Handling
- Use descriptive print statements for debugging (current approach)
- TODO: Implement proper logging and exception handling
- Validate CSV structure before processing transactions

### File Organization
- Keep data files in `./data/` directory
- Use descriptive module names (e.g., `category_loader.py`, `transaction_loader.py`)
- Separate data models from business logic

### Code Patterns
- Use match/case statements for category handling (Python 3.10+)
- Implement `__repr__` methods for debugging data classes
- Use list comprehensions for data transformation where appropriate