import numpy as np

input = np.loadtxt("Inputs/1.12.txt", dtype='str')

output = 0

for i in input:
    digOne = 0
    digTwo = 0
    j = 0
    while j <= (len(i)+1):
        try:
            digOne = digOne + int(i[j])
            break
        except:
            j += 1
    j = 0
    while j <= (len(i)+1):
        try:
            digTwo = digTwo + int(i[(len(i)+1)-j])
            break
        except:
            j += 1
    fullNum = int(str(digOne) + str(digTwo))
    output = output + fullNum
print(output)
