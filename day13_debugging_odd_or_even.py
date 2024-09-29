# Bug :
# def odd_or_even(number):
#    if number % 2 = 0:
#       return "This is an even number."
#    else:
#        return "This is an odd number."

# Bug is "if number % 2 = 0", should use "==" for comparisons

def odd_or_even(number):
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."