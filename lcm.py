a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x = a
y = b

while y != 0:
    x, y = y, x % y

if a == 0 or b == 0:
    print("LCM = 0")
else:
    lcm = abs(a * b) // x
    print("LCM =", lcm)
