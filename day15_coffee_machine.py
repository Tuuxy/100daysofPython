import os
import time
import day15_data


def clear_screen():
    """Function to clean the screen"""
    return os.system("cls") if os.name == "nt" else os.system("clear")

def prompt_user():
    """Function to check the user's coffee choice, off turns off the coffee machine, report gives a resources report"""
    while True:
        user_choice = input("\nWhat would you like? espresso/latte/cappuccino: \n").lower()
        if user_choice == "off":
            print("Turning off the coffee machine...")
            return False
        elif user_choice == "report":
            for key in day15_data.resources:
                print(f"{key}: {day15_data.resources[key][0]}{day15_data.resources[key][1]}")
            return True
        elif user_choice == "refill":
            print("Refilling the machine ...")
            for ingredient in ["water","milk","coffee"]:
                day15_data.resources[ingredient][0] = 1000
            return True
        elif user_choice in day15_data.MENU:
            return user_choice
        print("Invalid input. Please enter 'espresso','latte' or 'cappuccino'.")

def resources_checking(choice):
    """Check if the machine has enough resources to make the asked coffee"""
    ingredients = retrieve_ingredients(choice)
    enough_resource = True
    
    for ingredient in ingredients:
        name, amount = ingredient
        if amount > day15_data.resources[name][0]:
            print(f"Sorry there is not enough {name}.")
            enough_resource = False
    return enough_resource

def process_payment(choice):
    """Processes the payment, asks the user to insert coins and gives the change back"""
    COINS = {"quarters":0.25, "dimes":0.1, "nickles":0.05, "pennies":0.01}
    price = day15_data.MENU[choice]['cost']
    print(f"Please insert {price}$")
    total = 0
    while price > total:
        for coin in COINS:
            while total < price:
                try:
                    add_coin = int(input(f"Please enter your {coin} ({COINS[coin]}$): ")) * COINS[coin]
                    total += add_coin
                    if total < price:
                        print(f"Remaining: {price-total:.2f}$")
                    break
                except ValueError:
                    print(f"Invalid input. Please enter the number of {coin} you want to insert.")
        while total < price:
            try:
                not_enough = input("If you do not have enough coins to pay type 'stop', press Enter to add more coins. ").lower()
                if not_enough == "stop":
                    print("Sorry that's not enough money. Money refunded.")
                    return 0
                else:
                    break
            except ValueError:
                print("Invalid input.")

    print(f"Please retrieve your change: {total-price}$")
    return price

def retrieve_ingredients(choice):
    """Retrieve ingredients required to make the coffee"""
    ingredients = []

    for ingredient in day15_data.MENU[choice]['ingredients']:
        resource = [ingredient,day15_data.MENU[choice]['ingredients'][ingredient]]
        ingredients.append(resource)  
    return ingredients

def make_coffee(choice):
    """Function to actually make the coffee and deduct ingredients on the resources"""
    ingredients = retrieve_ingredients(choice)
    for ingredient in ingredients:
        name, amount = ingredient
        day15_data.resources[name][0] -= amount

    print(f"Here is your {choice}. Enjoy!")

def main():
    while True:
        coffee_type = prompt_user()
        if coffee_type == False:
            break
        if type(coffee_type) != bool:
            can_be_made = resources_checking(coffee_type)
            if can_be_made:
                money = process_payment(coffee_type)
                day15_data.resources["money"][0] += money
                make_coffee(coffee_type)
                time.sleep(5)
                clear_screen()
        else:
            input("Here is your report, press enter to continue.")
            clear_screen()

if __name__ == "__main__":
    main()
    