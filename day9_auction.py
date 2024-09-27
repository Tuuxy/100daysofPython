import os
import day9_art


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def main():
    auction = {}
    while True:
        print(day9_art.logo)
        name = input("What is your name?: ")
        while True:
            try:
                bid = float(input("What's your bid?: $"))
                break
            except:
                print("Invalid input. Please enter a valid number.")
        auction[name] = bid
        keep_going = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        if keep_going == "no":
            break
        clear_screen()

    winner = max(auction, key=auction.get)

    print(f"The winner is {winner} with a bid of ${auction[winner]:.2f}")

if __name__ == "__main__":
    main()