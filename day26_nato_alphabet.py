import pandas


def process_word(alphabet):
    """Return a list of the spelling of a word in the nato alphabet"""
    user_input = input("Enter a word: ").upper()
    return [alphabet[letter] for letter in user_input]

def yes_or_no(prompt):
    while True:
        user_input = input(prompt)
        if user_input == "y":
            return True
        elif user_input == "n":
            return False
        else:
            print("Please enter a correct value: 'y' or 'n'.\n")
        

if __name__ == "__main__":
    FILE = "day26_nato_alphabet.csv"
    DATA = pandas.read_csv(FILE)
    NATO_ALPHABET = {row.letter:row.code for (index, row) in DATA.iterrows()}
    
    keep_going = True
    while keep_going:

        word = process_word(NATO_ALPHABET)
        print(word)

        keep_going = yes_or_no("Do you want to keep going? 'y' or 'n'.\n")
    
    print("Bye!")