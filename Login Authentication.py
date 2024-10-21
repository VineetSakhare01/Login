

# Login Authentication using Conditional Statement. Assume you have a predefined username & password.
# Write a program that prompts the user to enter a username & password and checks whether they match.
# Provide Appropriate messages for the following cases.

# 1. Both username & password are correct.
# 2. Username is correct but password is incorrect.
# 3. Username is incorrect.


# User input
username = input("Enter your username: ")
password = input("Enter your password: ") 

# Declaring the assume username & password
a = "vineet"
b = "data01"

# Appling conditional statemnet
if username == a:
    if password == b:
        print("Welcome, you have successfully login!")
    else:
        print("Incorrect password, please try again.")
else:
    print("Username is incorrect.")        