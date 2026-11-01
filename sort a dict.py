data = {
    "Apple": 50,
    "Banana": 20,
    "Mango": 80,
    "Orange": 40
}

result = dict(sorted(data.items(), key=lambda x: x[1]))

print(result)
