import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

char_type = ["type_letter", "type_number", "type_symbol"]
password_length = nr_letters + nr_symbols + nr_numbers
password = ""


for i in range(password_length):

    if nr_letters == 0:
        if "type_letter" in char_type:
            char_type.remove("type_letter")
    if nr_numbers == 0:
        if "type_number" in char_type:
            char_type.remove("type_number")
    if nr_symbols == 0:
        if "type_symbol" in char_type:
            char_type.remove("type_symbol")
    
    char = random.choice(char_type)

    if char == "type_letter":
        nr_letters -= 1
        password += random.choice(letters)
    elif char == "type_number":
        nr_numbers -= 1
        password += random.choice(numbers)
    else :
        nr_symbols -= 1
        password += random.choice(symbols)

print(password)