import math

num = int(input("Enter a number: "))
total = 0

for digit in str(num):
    total += math.factorial(int(digit))

if total == num:
    print("Strong Number")
else:
    print("Not a Strong Number")
