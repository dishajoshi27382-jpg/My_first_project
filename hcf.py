def hcf(a, b):
    if b == 0:
        return abs(a)
    return hcf(b, a % b)

print("HCF =", hcf(24, 36))
