# Project-15
OOP Coffee machine
# Coffee Machine OOP ☕

An object-oriented coffee machine simulator built with Python classes. This version refactors the procedural coffee machine into a clean, modular OOP design.

## Project Structure
```
coffee-machine-oop/
│
├── main.py              # Main program loop
├── coffee_maker.py      # CoffeeMaker class - manages resources and brewing
├── menu.py              # Menu and MenuItem classes - manages drink options
└── money_machine.py     # MoneyMachine class - handles payments
```

## Requirements

- Python 3.x
- No external libraries needed

## How to Run
```bash
python main.py
```

## Classes Overview

### 1. **MenuItem** (menu.py)
Represents individual drink items with ingredients and pricing.

**Attributes:**
- `name` - Drink name
- `cost` - Price in dollars
- `ingredients` - Dictionary of required resources

### 2. **Menu** (menu.py)
Manages the collection of available drinks.

**Methods:**
- `get_items()` - Returns formatted string of drink names
- `find_drink(order_name)` - Searches for drink by name

**Available Drinks:**
- Latte: $2.50 (200ml water, 150ml milk, 24g coffee)
- Espresso: $1.50 (50ml water, 0ml milk, 18g coffee)
- Cappuccino: $3.00 (250ml water, 50ml milk, 24g coffee)

### 3. **CoffeeMaker** (coffee_maker.py)
Manages machine resources and coffee production.

**Attributes:**
- `resources` - Dictionary tracking water, milk, coffee levels

**Methods:**
- `report()` - Displays current resource levels
- `is_resource_sufficient(drink)` - Checks if enough ingredients available
- `make_coffee(order)` - Deducts ingredients and dispenses drink

**Starting Resources:**
- Water: 300ml
- Milk: 200ml
- Coffee: 100g

### 4. **MoneyMachine** (money_machine.py)
Handles all payment processing and profit tracking.

**Attributes:**
- `profit` - Total money collected
- `money_received` - Current transaction amount
- `COIN_VALUES` - Dictionary of coin denominations

**Methods:**
- `report()` - Displays total profit
- `process_coins()` - Prompts user for coin input and calculates total
- `make_payment(cost)` - Validates payment and processes transaction

**Accepted Coins:**
- Quarters: $0.25
- Dimes: $0.10
- Nickles: $0.05
- Pennies: $0.01

## How to Use

### Order a Drink
```
What would you like? latte/espresso/cappuccino/ latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is $0.0 in change.
Here is your latte ☕️. Enjoy!
```

### Check Resources & Profit
```
What would you like? latte/espresso/cappuccino/ report
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
```

### Turn Off Machine
```
What would you like? latte/espresso/cappuccino/ off
```

## Program Flow
```
1. Display menu options
2. User selects drink
3. Check if resources are sufficient
4. Process payment (coins)
5. Validate transaction
6. Deduct resources
7. Dispense drink
8. Loop back to step 1
```

## Key Features

✅ **Object-Oriented Design** - Clean separation of concerns  
✅ **Encapsulation** - Each class manages its own data  
✅ **Resource Management** - Automatic inventory tracking  
✅ **Payment Processing** - Coin counting and change calculation  
✅ **Validation** - Checks resources before accepting payment  
✅ **Reporting** - View machine status and profit  
✅ **Error Handling** - Insufficient resources and payment feedback  

## OOP Improvements Over Procedural Version

| Feature | Procedural | OOP |
|---------|-----------|-----|
| **Code Organization** | Single file, mixed concerns | Multiple classes, single responsibility |
| **Reusability** | Functions tied to global state | Classes can be reused/extended |
| **Maintainability** | Hard to modify | Easy to update individual classes |
| **Scalability** | Difficult to add features | Simple to extend with inheritance |
| **Testing** | Hard to test in isolation | Each class testable independently |

## Example Session
```
What would you like? latte/espresso/cappuccino/ espresso
Please insert coins.
How many quarters?: 6
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is $0.0 in change.
Here is your espresso ☕️. Enjoy!

What would you like? latte/espresso/cappuccino/ cappuccino
Sorry there is not enough water.

What would you like? latte/espresso/cappuccino/ report
Water: 250ml
Milk: 200ml
Coffee: 82g
Money: $1.5

What would you like? latte/espresso/cappuccino/ off
```

## What I Learned

Refactoring to OOP taught me:

- **Class design** - Creating classes with clear, single responsibilities
- **Encapsulation** - Keeping data and methods together in logical units
- **Object interaction** - How objects communicate through method calls
- **Attributes vs Methods** - When to use instance variables vs class constants
- **Constructor patterns** - Using `__init__()` to initialize object state
- **Separation of concerns** - Dividing program into Menu, CoffeeMaker, and MoneyMachine
- **Import statements** - Organizing code across multiple files
- **Instance creation** - Creating and using multiple objects from classes
- **Method chaining** - Calling methods on returned objects
- **Code modularity** - Making code easier to test, maintain, and extend

This project demonstrated the power of OOP for creating maintainable, scalable applications.

- Implement database for order history

Enjoy your virtual coffee! ☕
