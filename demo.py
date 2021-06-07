import random
def add(a, b):
    return a+b

def square(c):
    return c**2

for x in range(5):
    result = square(random.randint(1, 10))
    print(result)
