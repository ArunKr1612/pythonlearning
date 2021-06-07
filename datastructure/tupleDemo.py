# Tuple is similar to list, but it is immutible.
fruits = ('Apple', 'Banana', 'Grapes', 'orange')
# fruits[1] = 'Mango' // Not Possible will get TypeError: 'tuple' object does not support item assignment
print(fruits[1])
print(fruits[2:10])
print(fruits[:2])
print(fruits[3:])

# Tuple/list slicing

numbers = [1, 4, 6, 7, 9, 10, 37, 38, 87]  # defining list
print(numbers[2:7])
print(numbers[2:9:3])  # here third parameter is used to define interval of number to be print.
