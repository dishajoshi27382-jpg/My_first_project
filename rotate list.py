numbers = [1, 2, 3, 4, 5]

k = int(input("Enter rotation count: "))

k = k % len(numbers)

result = numbers[-k:] + numbers[:-k]

print("Rotated list:", result)
