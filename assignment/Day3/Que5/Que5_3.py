
def add(a, b):
    return a + b

def operate(a, b, func):
    return func(a, b)

result = operate(10, 5, add)
print("Result:", result)
