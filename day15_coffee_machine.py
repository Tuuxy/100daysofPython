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

        if user_choice == "report":
            print("\n\nHere is your report:\n")
            for key in day15_data.resources:
                print(f"{key}: {day15_data.resources[key][0]}{day15_data.resources[key][1]}")
            input("Press enter to continue.")
            return True
        
        if user_choice == "refill":
            print("Refilling the machine ...")
            for ingredient in ["water","milk","coffee"]:
                day15_data.resources[ingredient][0] = 1000
            time.sleep(3)
            return True

        if user_choice in day15_data.MENU:
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
    
    while total < price:
        for coin, value in COINS.items():
            try:
                count = int(input(f"Enter the number of {coin} ({value}$): "))
                total += count * value
                if total >= price:
                    break
                print(f"Remaining: {price-total:.2f}$")
            except ValueError:
                print(f"Invalid input. Please enter a valid number for {coin}.")
        
        if total < price:
            if input("Type 'stop' to cancel payment or press Enter to continue: ").lower() == 'stop':
                print("Sorry, that's not enough money. Money refunded.")
                return 0
    
    change = total - price
    if change > 0:
        print(f"Payment successful. Your change is {change:.2f}$")
    else:
        print("Payment successful.")
    return total

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

    print(f"Here is your {choice} ☕️. Enjoy!")

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
            clear_screen()

if __name__ == "__main__":
    main()
    