from C_M_menu import resources
from C_M_menu import MENU

machine = "on"
PENNY = 0.01
DIME = 0.10
NICKEL = 0.05
QUARTER = 0.25

# To create a function for to add values for the each items
def add_values(order):
    required_water = MENU[order]["items"].get("water",0)
    required_coffee = MENU[order]["items"].get("coffee",0)
    required_milk = MENU[order]["items"].get("milk",0)
    required_rate = MENU[order]["rate"]
    return required_water, required_coffee, required_milk, required_rate

# To create a function to calculate the cost
def coins_count_to_pay():
    print("Please insert the coins")
    a = float(input("How many Quarters? "))*0.25
    b = float(input("How many Dimes? "))*0.10
    c = float(input("How many Nickels? "))*0.05
    d = float(input("How many Pennys? "))*0.01
    sum = a+b+c+d
    return sum

while(machine!="off"):
    # TODO: To make an order
    order = input("What would you like? (expresso/latte/cappuccino): ").lower()

    # TODO: To print the report using report keyword
    if(order=="report"):
        water = resources.get("water")
        coffee = resources.get("coffee")
        milk = resources.get("milk")
        money = resources.get("money")
        print(f"Water: {water}ml \nCoffee: {coffee}g \nMilk: {milk}ml \nMoney: ${money}")

    # TODO: To turn off the machine
    if(order=="off"):
        machine = "off"

    # TODO: To check the resources are sufficient
    # To order expresso
    if(order=="expresso"):
        # Calling the function
        required_water, required_coffee, required_milk, required_rate = add_values(order)
        if(required_water <= resources["water"] and required_coffee <= resources["coffee"]):
            # calling the function
            sum = coins_count_to_pay()
            if sum >= required_rate:
                rem_amount = round(sum - required_rate, 2)
                if rem_amount > 0:
                    print(f"Here is ${rem_amount} in change")
                    print(f"Here is your {order} ☕, Enjoy!!")
                    # TODO: To reduce the amount of resources based on the order
                    resources["water"] -= required_water
                    resources["coffee"] -= required_coffee
                    resources["money"] += required_rate
            else:
                print(f"Sorry that's not enough money. Your money ${sum} is refunded.")
        else:
            print("Sorry, There is no enough Water")

    # To order latte
    if(order=="latte"):
        # Calling the function
        required_water, required_coffee, required_milk, required_rate = add_values(order)

        if(required_water <= resources["water"] and required_coffee <= resources["coffee"] and required_milk <= resources["milk"]):
            # calling the function
            sum = coins_count_to_pay()

            if sum >= required_rate:
                rem_amount = round(sum - required_rate, 2)
                if rem_amount > 0:
                    print(f"Here is ${rem_amount} in change")
                    print(f"Here is your {order} ☕, Enjoy!!")
                    # TODO: To reduce the amount of resources based on the order
                    resources["water"] -= required_water
                    resources["coffee"] -= required_coffee
                    resources["milk"] -= required_milk
                    resources["money"] += required_rate
            else:
                print(f"Sorry that's not enough money. Your money ${sum} is refunded.")
        else:
            print("Sorry, There is no enough Water")

    # To order cappuccino
    if(order=="cappuccino"):
        # Calling the function
        required_water, required_coffee, required_milk, required_rate = add_values(order)

        if(required_water <= resources["water"] and required_coffee <= resources["coffee"] and required_milk <= resources["milk"]):
            # calling the function
            sum = coins_count_to_pay()
            
            if sum >= required_rate:
                rem_amount = round(sum - required_rate, 2)
                if rem_amount > 0:
                    print(f"Here is ${rem_amount} in change")
                    print(f"Here is your {order} ☕, Enjoy!!")
                    # TODO: To reduce the amount of resources based on the order
                    resources["water"] -= required_water
                    resources["coffee"] -= required_coffee
                    resources["milk"] -= required_milk
                    resources["money"] += required_rate
            else:
                print(f"Sorry that's not enough money. Your money ${sum} is refunded.")
        else:
            print("Sorry, There is no enough Water")

    
    