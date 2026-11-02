import hashlib

message = input("Enter a message: ")

result = hashlib.sha256(
    message.encode()
).hexdigest()

print("SHA-256 Hash:", result)
