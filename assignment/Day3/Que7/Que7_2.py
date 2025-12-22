
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print("2 raised to power 4:", power(2, 4))
print("2 raised to power 24:", power(2, 24))
print("2 raised to power 100:", power(2, 100))
print("2 raised to power 12:", power(2, 12))
print("2 raised to power 98:", power(2, 98))
print("2 raised to power 43:", power(2, 43))
print("2 raised to power 45:", power(2, 45))
print("2 raised to power 65:", power(2, 65))
print("2 raised to power 9:", power(2, 9))
