
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))
print("Factorial of 0:", factorial(0))
print("Factorial of 19:", factorial(19))
print("Factorial of 22:", factorial(22))
print("Factorial of 59:", factorial(59))
print("Factorial of 45:", factorial(45))
print("Factorial of 50:", factorial(50))
print("Factorial of 10:", factorial(10))
print("Factorial of 1:", factorial(1))
