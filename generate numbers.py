def generate_numbers():
    for i in range(1, 6):
        yield i

for num in generate_numbers():
    print(num)
