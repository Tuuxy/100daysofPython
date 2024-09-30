import os
import random
import day14_art
import day14_data

def clear_screen():
    """Function to clean the screen"""
    return os.system("cls") if os.name == "nt" else os.system("clear")

def display(a,b,score):
    print(day14_art.logo)
    if score > 0 :
        print(f"You're right! Current score: {score}.")
    print(f"Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}.")
    print(day14_art.vs)
    print(f"Compare B: {b["name"]}, a {b["description"]}, from {b["country"]}.")

def validate_response(prompt,valid):

    while True:
        response = input(prompt).lower()
        if response in valid:
            return response
        print("Invalid input.")

def get_data(previous_b,score):
    a = previous_b if score != 0 else random.choice(day14_data.data)
    while True :
        b = random.choice(day14_data.data)
        if b != a:
            break
    previous_b = b
    return a, b, previous_b

def compare_answer(answer,a,b):
    correct = max(a["follower_count"],b["follower_count"])
    player_response = a["follower_count"] if answer == "a" else b["follower_count"]
    
    if player_response == correct:
        return True
    else :
        return False 

def main():
    while True:
        score = 0
        previous_b = None
        while True:
            a, b, previous_b = get_data(previous_b,score)
            clear_screen()
            display(a,b,score)
            answer = validate_response("Who has more followers? Type 'A' or 'B': ",["a","b"])
            answer_is_correct = compare_answer(answer,a,b)
            if answer_is_correct:
                score += 1
            else :
                print(f"Sorry that's wrong. Final score: {score}")
                break

        keep_playing = validate_response("Do you want to keep playing? If yes, type 'y' else type 'n'. ",["y","n"])

        if keep_playing == "n":
            print("Thank you for playing. Goodbye!")
            break
    
        
        
    

if __name__ == "__main__":
    main()
