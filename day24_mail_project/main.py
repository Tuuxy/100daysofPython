def store_names(path):
    with open(path,"r") as names_file:
        return [name.strip() for name in names_file.readlines()]
    
def read_letter(path):
    with open(path,"r") as letter_file:
        return letter_file.read()

def create_letters(names, letter_content, output_directory):
    PLACEHOLDER = "[name]"

    for name in names:
        new_letter = letter_content.replace(PLACEHOLDER, name)
        output_path = f"{output_directory}/letter_for_{name}.txt"
        with open(output_path,"w") as completed_letter:
            completed_letter.write(new_letter)


if __name__ == "__main__":
    names = store_names("./Input/Names/invited_names.txt")
    letter_content = read_letter("./Input/Letters/starting_letter.txt")
    create_letters(names, letter_content, "./Output/ReadyToSend")