students = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 78,
    "Sneha": 89
}

for name, marks in students.items():
    print(name, ":", marks)

average = sum(students.values()) / len(students)

print("Average marks:", average)
