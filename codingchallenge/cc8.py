# List out  all the odd numbers from 1 to 100 using lists in Python.

oddList = [x for x in range(1, 100) if x % 2 != 0]
print(oddList)