def compound_interest(p, r, t):
    amount = p * (1 + r / 100) ** t
    return amount - p

print("Compound Interest =", compound_interest(10000, 5, 2))
