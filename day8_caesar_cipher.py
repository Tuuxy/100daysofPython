import day8_art


print(day8_art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, method):
    output = ""
    shift_amount = shift_amount if method != "decode" else -shift_amount
    for letter in original_text:
        if letter in alphabet:
            index = (alphabet.index(letter) + shift_amount) % len(alphabet)
            output += alphabet[index]
        else:
            output += letter
    return f"Here is your {method}d result: {output}"

def main():
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction != 'encode' and direction != 'decode':
            print("Invalid input. Please enter 'encode' or 'decode'.")
            continue
        text = input("Type your message:\n").lower()
        while True:
            try:
                shift = int(input("Type the shift number:\n"))
                break
            except:
                print("Invalid input. Please enter a valid number for the shift.")
        print(caesar(original_text=text, shift_amount=shift, method=direction))
        keep_going = input("Type 'yes' if you want to go again. Otherwise, type 'no'.")
        if keep_going == "no":
            print("Goodbye.")
            break

if __name__ == "__main__":
    main()
