import re

number = input("Enter mobile number: ")

pattern = r"^[6-9][0-9]{9}$"

if re.fullmatch(pattern, number):
    print("Valid Indian mobile number format")
else:
    print("Invalid mobile number format")
