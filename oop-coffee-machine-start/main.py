from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money_machine = MoneyMachine()

start = "on"
while start != "off":
    items = menu.get_items()
    choice = input(f"What would you like to order? {items}: ").lower()

    # To turn off the machine
    if choice == "off":
        print("The ☕ machine is off 🫨")
        restart = input("Do you want to turn it on? ").lower()
        if restart == "yes":
            start = "on"
        else:
            start = "off"
    
    # To print the report
    elif choice == "report":
        coffee.report()
        money_machine.report()

    # To make coffee
    else:
        drinkName = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drinkName) and money_machine.make_payment(drinkName.cost):
            coffee.make_coffee(drinkName)


    

