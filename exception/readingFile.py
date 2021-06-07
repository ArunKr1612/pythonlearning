file = open("D:/python/FirstProject/resource/firstFile.txt", "rw")
for x in file.readlines():
#print(content)
    if x.__contains__('python'):
        file.write('java')
    else:
         print('No selected values')
         print(x)
file.close()