while True:
    print("\n1. Check balance")
    print("2. Deposit")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance: Rs. 5000")
    elif choice == 2:
        amount = int(input("Enter amount: "))
        print("Deposit amount:", amount)
    elif choice == 3:
        print("Thank you!")
        break
    else:
        print("Invalid choice")
