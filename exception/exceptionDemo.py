def func1(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print('Divide by zero exception')
    finally:
        print('In finally block')

print(func1(2, 1))
print('Exception handled')