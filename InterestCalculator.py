username = input('Enter UserName : ')
password = input('Enter Password : ')
values = [1, 2, 3]
def continueF():
    y = input('Do you want to Continue (y/n): ')
    return y

def simpleInterest(p, n, r):
    i = (p*r*n)/100
    return i

if username == 'admin' and password == 'admin123':
    result = continueF()
    while(result == 'y' or result == 'yes'):
        if result.__eq__('y') or result.__eq__('yes'):
            p = int(input('Enter Principle Amount : '))
            r = int(input('Enter ROI : '))
            n = int(input('No Of Year : '))
            si = simpleInterest(p, n, r)
            print('Simple Interest : ', si)
        elif result.__eq__('n') or result.__eq__('no'):
            break
        result = continueF()
else:
    print('Enter valid username/password')



