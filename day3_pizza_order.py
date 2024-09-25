print("Welcome to Python Pizza Deliveries!")
prices = {"small_pizza":15,"medium_pizza":20,"large_pizza":25,"pepperoni_small":2,"pepperoni_medium_large":3,"cheese":1}

while True:

    bill = 0
    size = input("What size pizza do you want? S, M or L:\n")
    if size == "S":
        bill += prices["small_pizza"]
        pepperoni = input("Do you want pepperoni on your pizza? Y or N:\n ")
        if pepperoni == "Y":
            bill += prices["pepperoni_small"]
        extra_cheese = input("Do you want some extra cheese? Y or N:\n")
        if extra_cheese =="Y":
            bill += prices["cheese"]
    elif size == "M":
        bill += prices["medium_pizza"]
        pepperoni = input("Do you want pepperoni on your pizza? Y or N:\n ")
        if pepperoni == "Y":
            bill += prices["pepperoni_medium_large"]
        extra_cheese = input("Do you want some extra cheese? Y or N:\n")
        if extra_cheese =="Y":
            bill += prices["cheese"]
    elif size == "L":
        bill += prices["large_pizza"]
        pepperoni = input("Do you want pepperoni on your pizza? Y or N:\n ")
        if pepperoni == "Y":
            bill += prices["pepperoni_medium_large"]
        extra_cheese = input("Do you want some extra cheese? Y or N:\n")
        if extra_cheese =="Y":
            bill += prices["cheese"]
    else:
        print("Pizza size incorrect.")
        continue

    print(f"Your bill is ${bill}.")

    state = input("Continue? Y or N:\n")
    
    if state == "N":
        break