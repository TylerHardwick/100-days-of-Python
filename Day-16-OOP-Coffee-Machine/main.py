from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


drinks = Menu()
vend = CoffeeMaker()
money = MoneyMachine()
continue_vending = True

while continue_vending:

    chosen_drink = input(f"What would you like? ({drinks.get_items()}): ").lower()
    if chosen_drink == "report":
        vend.report()
        money.report()
    elif chosen_drink == "off":
        print("Powering off Coffee Machine.")
        continue_vending = False
    else:
        drink_in_menu = drinks.find_drink(chosen_drink)
        if vend.is_resource_sufficient(drink_in_menu) and money.make_payment(drink_in_menu.cost):
            vend.make_coffee(drink_in_menu)
