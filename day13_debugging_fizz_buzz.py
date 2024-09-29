# Bug: 
#def fizz_buzz(target):
#    for number in range(1, target + 1):
#        if number % 3 == 0 or number % 5 == 0:
#            print("FizzBuzz")
#        if number % 3 == 0:
#            print("Fizz")
#        if number % 5 == 0:
#            print("Buzz")
#        else:
#            print([number])
# Bug are "number % 3 == 0 or number % 5 == 0" should be "and" and not "or", then since every condition
# is an "if" then number that are divisible by 3 and 5 are printed twice, so we should use "elif"
# and we need to print the number not a list of number so instead of "print([number])" it should be "print(number)"

def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

fizz_buzz(20)