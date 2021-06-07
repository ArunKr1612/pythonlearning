# This is used to display string in defined format.

str = "{x}/{y}".format(x=100, y=20)
print(str)

# String function
# 1. join() -> it is used to join a string to list.

fruits = ['Apple', 'Banana', 'Mango']
print('|'.join(fruits))  # Result = Apple|Banana|Mango

# 2. replace()

print('Hello Java'.replace('Java', 'python'))

# 3. startswith()
print('Hi, hw are you'.startswith('Hi'))

# 4. endswith()
print('Hello Java'.endswith('python'))

# 5. upper()
print('hello'.upper())

# 6. lower()
print('HELLO'.lower())



