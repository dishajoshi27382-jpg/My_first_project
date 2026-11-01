text = input("Enter a message: ")
shift = 3

result = ""

for ch in text:
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        result += chr((ord(ch) - base + shift) % 26 + base)
    else:
        result += ch

print("Encoded message:", result)
