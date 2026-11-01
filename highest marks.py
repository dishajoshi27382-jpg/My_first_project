students = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 78,
    "Sneha": 89
}

topper = max(students, key=students.get)

print("Topper:", topper)
print("Marks:", students[topper])
