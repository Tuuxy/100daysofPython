import random 


def print_move(side):
    rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """

    paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    """

    scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """

    if side == "rock":
        print(rock)
    elif side == "paper":
        print(paper)
    else :
        print(scissors)

def who_wins(player,computer):
    if player == computer:
        return "It's a draw."
    winning_combinations = {"rock":"scissors", "paper":"rock", "scissors":"paper"}
    
    return "You win!" if winning_combinations[player] == computer else "You lose!"

def player_choice():
    while True:
        prompt = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
        
        if prompt not in ["0","1","2"]:
            print("Value out of range.")
            continue
        
        player_move = moves[int(prompt)]
        
        return player_move

moves = ["rock","paper","scissors"]

player_move = player_choice()
computer_move = random.choice(moves)

print_move(player_move)
print("Computer chose:")
print_move(computer_move)
print(who_wins(player_move,computer_move))


