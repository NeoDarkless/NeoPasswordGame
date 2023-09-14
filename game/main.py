import time

rules = [
    "1. Your password must be at least 10 characters.", 
    "2. Your password must be at most 70 characters.", 
    "3. Your password must have at least 3 digits.",
    "4. Every digit in your password must be unique.", 
    "5. Your password must have at least 5 special characters.", 
    "6. Your password must contain the current hour.", 
    "7. Your password must contain the current day of the week.", 
    "8. Every letter in your password must aLtErNaTe BeTwEeN lowercase and UPPERCASE."
    ]

def check_pass(pass):
    #1. Your password must be at least 10 characters.
    if len(pass) < 10:
        rule1 = False
        print(rules[0])
    #2. Your password must be at most 70 characters.
    if len(pass) > 70:
        rule2 = False
        print(rules[1])
    #3. Your password must have at least 3 digits.
    numeric_pass = pass
    for x in numeric_pass:
        if not x.isnumeric():
            numeric_pass.replace(x, "")


while True:
    password = input("Please choose a password. > ")
    check_pass(password)