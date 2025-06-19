ini = 8751
tempstr = ''
ini_s = str(ini)
for i in ini_s:
    temp = int(i)
    temp = temp **2
    tempstr += str(temp)

tempstr = int(tempstr)
print(tempstr)
print(type(tempstr))