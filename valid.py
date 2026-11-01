email = input("Enter your email: ")

if "@" in email and "." in email.split("@")[-1]:
    print("Basic email format is valid")
else:
    print("Invalid email format")
