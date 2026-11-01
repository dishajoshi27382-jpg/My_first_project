text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch != " ":
        frequency[ch] = frequency.get(ch, 0) + 1

if frequency:
    result = max(frequency, key=frequency.get)
    print("Most frequent character:", result)
    print("Frequency:", frequency[result])
else:
    print("No characters found")
