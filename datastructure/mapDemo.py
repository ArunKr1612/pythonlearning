# In python Map is used to apply function to any iterable object like list
def add_two(x):
    return x + 2

numberlist = [ 2, 4, 6, 8 ]

result = list(map(add_two, numberlist))
print(result)

print(list(map(lambda x : x+2, numberlist)))