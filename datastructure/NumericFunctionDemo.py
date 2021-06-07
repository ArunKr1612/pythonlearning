import random
# 1. min()
# print(min(1, 2, 3, 6, 8))

# find the min value from number list
randomNumbers = []
for x in range(5):
    n = random.randint(5, 19)
    randomNumbers.append(n)
print(randomNumbers)

# find min, max without using function from list.

def minmax(y):
    minimum = maximum = y[0]
    for i in y[1:]:
        if i < minimum:
            minimum = i
        else:
            if i > maximum:
                maximum = i
    return(minimum, maximum)

print(lambda a,b : a if a < b else b, randomNumbers[0] ,randomNumbers[1:])

#print(minmax([3, 7, 9, 1, 2, -54, -2]))



