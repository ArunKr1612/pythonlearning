evenList = [x**2 for x in range(1, 11) if x**2 % 2 == 0]
print(evenList)

# student list whose name starts with A
students = ['Arun', 'Amit', 'Amar', 'Ram', 'Ravi', 'Mukesh']

studentNameStartWithA = [x for x in students if x.startswith('A')]
print(studentNameStartWithA)
