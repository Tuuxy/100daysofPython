import random
from day7_hangman_art import stages, logo
from day7_hangman_words import word_list


def print_stage(life):
    return stages[life-7]

def change_display(display,index,letter):
    display_list = [i for i in display]
    display_list[index] = letter
    display = "".join(display_list)
    return display

def generate_word(word_list):
    return random.choice(word_list)

print(logo)
word = generate_word(word_list)
display = "_" * len(word)
print(display)
life = 6

already_guessed = []

while life > 0:
    
    guess = input("Guess a letter : ").lower()

    if guess in already_guessed:
        print("You already guessed this letter.")
        continue
    
    already_guessed += guess

    for i in range(len(word)):
        if word[i] == guess:
            display = change_display(display,i,guess)
    
    if guess not in word:
        life -= 1
        print(f"Letter {guess} not in the word.\nRemaining lifes:{life}")

    if display == word:
        print(f"Word was {word}")
        print("***** You won! *****")
        break
    print(display)
    print(print_stage(life))

if life == 0 :
    print(f"Word was {word}")
    print("***** You lose! *****")