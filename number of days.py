import calendar

year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

days = calendar.monthrange(year, month)[1]

print("Days in month:", days)
