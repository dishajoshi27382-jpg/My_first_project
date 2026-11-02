from datetime import date

date1 = date(2026, 1, 1)
date2 = date(2026, 12, 31)

difference = abs((date2 - date1).days)

print("Difference:", difference, "days")
