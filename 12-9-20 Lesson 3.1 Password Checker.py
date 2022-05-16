#Lesson 3.1 Password Checkers
#Jasmin Salgado
#CP1
#12/9/20

password = input("Enter a password: ")

#Set variable to Boolean value (True False)
length = False
hasUpper = False
hasLower = False
hasDigit = False

numbers = '1234567890'
lowers = 'abcdefghijhklmnopqrstuvwxyz'
uppers = lowers.upper()

#Check if the length of the password, adjust boolean value accordingly
for characters in password:
    if len(password) >= 8:
        length = True
#Check is there are numbers in the password and adjust boolean value accordingly
for characters in password:
    if characters in numbers:
        hasDigit = True
#Check is there are lower case in the password and adjust boolean value accordingly
for characters in password:
    if characters in lowers:
        hasLower = True
#Check is there are upper case in the password and adjust boolean value accordingly
for characters in password:
    if characters in uppers:
        hasUpper = True

#If all conditions are met output value password, other tell user what is missing
if length and hasDigit and hasLower and hasUpper:
    print("password is valid")
else:
    print("invalid password")
    
    if length == False:
        print("password must have at least 8 characters")
        if hasDigit == False:
            print("password must have at least 1 digit")
            if hasLower == False:
                print("password must have at least 1 lowercase letter")
            elif hasUpper == False:
                print("password must have at least 1 uppercase letter")
        elif hasLower  == False:
            print("password must have at least 1 lowercase letter")
            if hasUpper == False:
                print("password must have at least 1 uppercase letter")
        elif hasUpper == False:
            print("password must have at least 1 uppercase letter")  
            if hasLower == False:
                print("password must have at least 1 lowercase letter")
                
    elif hasDigit == False:
        print("password must have at least 1 digit")
        if hasLower == False:
            print("password must have at least 1 lowercase letter")
        elif hasUpper == False:
            print("password must have at least 1 uppercase letter")

    elif hasLower == False:
        print("password must have at least 1 lowercase letter")
        if hasUpper == False:
            print("password must have at least 1 uppercase letter")
        
    elif hasUpper == False:
        print("password must have at least 1 uppercase letter")
