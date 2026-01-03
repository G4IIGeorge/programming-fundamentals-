"""
Password strength checker.
Built to practice strings, loops, and conditionals.
"""

password = input("Enter a password: ")
has_length = len(password) >= 8
has_number = False
has_upper = False
has_special = False

for char in password:
    if char.isdigit():
        has_number = True
    elif char.isupper():
        has_upper = True
    elif char in "!@#$%^&*":
        has_special = True
    
score = 0

if has_length:
    score += 1
if has_number:
    score += 1
if has_upper:
    score += 1
if has_special:
    score += 1

if score <= 1:
    print("Weak password")
elif score <= 3:
    print("Medium password")
else:
    print("Strong password")
    