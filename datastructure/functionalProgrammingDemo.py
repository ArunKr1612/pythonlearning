# In functional programming we call function inside function.
def add_ten(x):
    return x + 10

def add_five(x):
    return x + 5

def three(func, arg):
    return func(func(add_five(arg)))

print(three(add_ten, 10))

