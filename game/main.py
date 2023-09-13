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

def check_pass(password):
    #1. Your password must be at least 10 characters.
    if len(password) < 10:
        rule1 = False
        print(rules[0])
    #2. Your password must be at most 70 characters.
    if len(password) > 70:
        rule2 = False
        print(rules[1])
    #3. Your password must have at least 3 digits.
    numeric_pass = password
    for x in numeric_pass:
        print(x)
        if not x.isnumeric():
            numeric_pass.replace(x, "")
    print(numeric_pass)


while True:
    password = input("Please choose a password. > ")
    check_pass(password)