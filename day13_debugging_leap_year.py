# Bug :
#def is_leap(year):
#    if year % 4 == 0:
#        if year % 100 == 0:
#            if year % 4000 == 0:
#                return True
#            else:
#                return False
#        else:
#            return True
#    else:
#        return False
# Bug is "if year % 4000 == 0", this is a typo, this should be 400

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else :
                return False
        else:
            return True
    else: 
        return False