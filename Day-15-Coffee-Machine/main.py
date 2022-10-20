from data import MENU
from data import resources

profit = 0


def coffee_select():
    """User selects coffee. Returns coffee."""
    coffee = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
    return coffee


def report():
    """Prints a list of remaining resources."""
    print(f"Water: {resources['water']}ml ")
    print(f"Milk: {resources['milk']}ml ")
    print(f"Coffee: {resources['coffee']}g ")
    print(f"Profit: {profit:.2f}")


def check_resources(drink):
    """Checks if resources available to make drink. If report is entered prints a report"""
    if drink == "report":
        report()
        return False
    elif drink == "off":
        print("Coffee machine is being powered off.")
        return False
    for ingredient in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    else:
        return True


def coin_check():
    print("Please insert coins.")
    quarters = float(input("How many Quarters?: ")) * 0.25
    dimes = float(input("How many Dimes?: ")) * 0.10
    nickles = float(input("How many Nickles?: ")) * 0.05
    pennies = float(input("How many Pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total


def make_drink(drink):
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]



def vend():
    deposit = coin_check()
    if deposit < MENU[chosen_drink]["cost"]:
        print("Sorry that is not enough money. Money refunded.")
        return 0
    else:
        make_drink(chosen_drink)
        change = deposit - MENU[chosen_drink]["cost"]
        print(f"Here is your ${change:.2f} in change.")
        print(f"Here is your {chosen_drink} ☕. Enjoy!")
        return profit + MENU[chosen_drink]["cost"]


machine_on = True
while machine_on:
    chosen_drink = coffee_select()
    if chosen_drink == "off":
        machine_on = False
    continue_vending = check_resources(chosen_drink)
    if continue_vending:
        profit += vend()

