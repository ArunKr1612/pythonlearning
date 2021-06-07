def even_number(x):
    for i in range(x):
        if i % 2 == 0:
            yield i


print(list(even_number(21)))
