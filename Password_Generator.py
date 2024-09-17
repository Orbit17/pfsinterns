# Creates a randomized password using user entered criteria
# User enters length and character style

import random
import string

key = ["!", "@" , "#", "$", "%", "&"] # used for special characters

print("Welcome to Random Password Generator!")
length = input("Enter a password length or \"exit\" to exit: ")

while(not length.isdigit() or int(length) <= 0): # checks for valid first input
        print("Retry. Enter a positive valid number for length")
        print("*"*8)
        length = input("Enter a password length or \"exit\" to exit: ")
        if length.lower() == "exit":
            break
    
while(length.lower() != "exit"): # enters into loop
    try:
        while(int(length) <= 0):
            if int(length) == 0:
                print("Length has to be greater than 0.")
            else:
                print("Retry. Enter a positive valid number for length")
                print("*"*8)
            
            length = input("Enter a password length or \"exit\" to exit: ")
            if length.lower() == "exit":
                break
    except ValueError:
            print("Input has to be a number.")
            length = input("Enter a password length or \"exit\" to exit: ")
            continue

    style = input("Enter a password style (1 for numbers, 2 for letters only, 3 for alphanumeric): ")
    password = ""

    if(style == "1"):
        for i in range(0, int(length)):
            password += str(random.randrange(0,10)) # generates a random number from 0 to 9
    elif(style == "2"):
        for i in range(0, int(length)):
            password += chr(random.randint(ord('a'), ord('z'))) # generates random letters using unicode values
    elif(style == "3"):
        for i in range(0, int(length)):
            password += random.choice(string.ascii_letters + string.digits + "".join(key)) # randomly chooses between a letter, digit, or special character
    else:
        print("Choose between 1, 2, or 3")
        continue

    print(password)

    length = input("Enter a password length or \"exit\" to exit: ")