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

rule1 = rule2 = rule3 = rule4 = rule5 = rule6 = rule7 = rule8 = None

def check_pass(password):
    # 1. Your password must be at least 10 characters.
    if len(password) < 10:
        rule1 = False
        print(rules[0])


print("Please choose a password.")