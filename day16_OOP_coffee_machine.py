from day16_menu import Menu, MenuItem
from day16_coffee_maker import CoffeeMaker
from day16_money_machine import MoneyMachine

def prompt_user(prompt,valid):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid:
            return user_input
        print("Invalid input. Valid inputs:")
        for valid_input in valid:
            print(valid_input)

def main():

    menu = Menu()
    options = menu.get_items()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while True:
        coffee_type = prompt_user(f"What would you like? {options}\n",["refill","off","report","espresso","latte","cappuccino"])

        if coffee_type == "off":
            print("Turning off the coffee machine...")
            break

        elif coffee_type == "report":
            coffee_maker.report()
            money_machine.report()

        elif coffee_type == "refill":
            coffee_maker.refill()

        else:
            menu_item = menu.find_drink(coffee_type)

            if menu_item is not None:
                if coffee_maker.is_resource_sufficient(menu_item):
                    if money_machine.make_payment(menu_item.cost):
                        coffee_maker.make_coffee(menu_item)


if __name__ == "__main__":
    main()