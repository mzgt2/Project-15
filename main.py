from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
drinks = menu.get_items()

while True:


    choice = input(f"What would you like? {drinks} ")
    beverage = menu.find_drink(choice)
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        exit()
    elif choice in drinks:
        enough = coffee_maker.is_resource_sufficient(beverage)
        if enough:
            result = money_machine.make_payment(beverage.cost)
            if result:
                coffee_maker.make_coffee(beverage)
    else:
        print("Invalid input.")
