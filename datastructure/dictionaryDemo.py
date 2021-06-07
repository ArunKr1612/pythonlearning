p = input('Get person age : ')
person = {"Jhon": 32, "Rob": 24}
try:
    if p in person:
        print(person.get(p))
    else:
        print("No person info.")
except KeyError:
    print("No person info with this name.")
