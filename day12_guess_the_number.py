import random
import os 
import day12_art

life = 0 

def clear_screen():
    """Function to clean the screen"""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def greetings():
    """Greets the player and prints the logo."""
    print(day12_art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

def difficulty():
    """Sets the difficulty level of the game."""
    valid = ["easy","hard"]
    while True:
        difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty_level in valid:
            break
        print("Invalid input.")
    
    return 10 if difficulty_level == valid[0] else 5

def guess():
    """Validates the guess number of the player"""
    valid = [str(i) for i in range(1,100)]
    while True:
        player_guess = input("Make a guess: ")
        if player_guess in valid:
            player_guess = int(player_guess)
            break
        print("Invalid input.")
    
    return player_guess

def compare(player_num,computer_num):
    """Compare the player number with the computer deduct life if they are different."""
    global life
    if player_num == computer_num:
        print(f"You got it! The answer was {computer_num}")
        return True
    else :
        life -= 1
        result = "Too high." if player_num > computer_num else "Too low."
        print(result)
        print(f"You have {life} attempts remaining to guess the number.")
        return False

def play_again():
    """Asks the player if he wants to continue playing or not."""
    valid = ["y","n"]
    while True:
        keep_playing = input("Do you want to play again? Type 'y' for yes or 'n' for no: ")
        if keep_playing in valid:
            break
        print("Invalid input.")
    return True if keep_playing == valid[0] else False

def play(COMPUTER_NUM):
    while life > 0:
        player_num = guess()
        won = compare(player_num,COMPUTER_NUM)
        if won == True:
            return True
    print("You've run out of guesses, you lose.")
    return False

def main():
    global life
    greetings()
    life = difficulty()
    COMPUTER_NUM = random.randint(1,100)

    game = play(COMPUTER_NUM)
    new_game = play_again()

    if new_game == True:
        clear_screen()
        main()
    else:
        print("Thanks for playing. Goodbye!")


if __name__ == "__main__":
    main()