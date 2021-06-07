w = float(input('Enter your Weight in Kg: '))
h = float(input('Enter your height in meter: '))

def getBMIVal(weight, height):
    return weight/height**2

print('Your BMI value is : ', getBMIVal(w, h))