import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Marks"])
    writer.writerow(["Rahul", 20, 85])
    writer.writerow(["Priya", 21, 90])

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
