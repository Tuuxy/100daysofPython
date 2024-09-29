import random
import os
import day11_art


VALUES = {
    1 : 11,
    2 : 2,
    3 : 3,
    4 : 4,
    5 : 5,
    6 : 6,
    7 : 7,
    8 : 8,
    9 : 9,
    10 : 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10,
}

def clear_screen():
    """Function to clean the screen"""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def make_deck():
    """Creates the deck"""
    deck = []
    for card in VALUES:
        for i in range(4):
            deck.append(card)
    return deck 

def draw(deck,cards=None,amount=1):
    """Draw x amount of cards"""
    if cards is None:
        cards = []
    for _ in range(amount):
        card = random.choice(deck)
        deck.remove(card)
        cards.append(card)
    return cards

def score(cards):
    """Calculate score of player/computer cards"""
    total_score = sum(VALUES[card] for card in cards)
    aces = cards.count(1)
    while total_score > 21 and aces:
        total_score -= 10
        aces -= 1
    return total_score

def yes_no(prompt):
    """Function to validate y/n answers"""
    valid = ["y","n"]
    while True:
        answer = input(prompt).lower()
        if answer in valid:
            break
        print("Invalid Input.")
    return True if answer == "y" else False

def who_wins(player,player_score,computer,computer_score):
    """Define who wins and display text"""

    print(f"Your final hand: {player}, final score: {player_score}")
    print(f"Computer's final hand: {computer}, final score: {computer_score}")

    if player_score == computer_score:
        return print("It's a draw.")
    if computer_score > 21:
        return print("Opponent went over. You win.")
    if computer_score == 21:
        return print("Lose, opponent has Blackjack.")
    if player_score == 21:
        return print("Win with a Blackjack")
    if player_score > computer_score:
        return print("You win.")
    else:
        return print("You lose.")

def main():

    deck = make_deck()
    player = draw(deck,amount=2)
    computer = draw(deck,amount=2)

    player_score = score(player)
    computer_score = score(computer)

    print(f"Player cards: {player}, score: {player_score}")
    print(f"Computer's first card: {computer[0]}")

    while True:
        drawing_more = yes_no("Type 'y' to get another card, type 'n' to pass: ")
        if drawing_more == False:
            break
        player = draw(deck,player,1)
        player_score = score(player)
        print(f"Your cards: {player}, current score: {player_score}")
        print(f"Computer's first card: {computer[0]}")

        if player_score > 21:
            return print("You went over. You lose.")


    while computer_score < 16:
        computer = draw(deck,computer,1)
        computer_score = score(computer)
    
    player_score = score(player)
    computer_score = score(computer)
    who_wins(player,player_score,computer,computer_score)


if __name__ == "__main__":
    while True:
        
        game = yes_no("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if game == False:
            print("Good Bye.")
            break
        clear_screen()
        print(day11_art.logo)
        main()
        
