numbers = [10, 20, 30, 40, 50]

key = int(input("Enter number to search: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == key:
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Element not found")
