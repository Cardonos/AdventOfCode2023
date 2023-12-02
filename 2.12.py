data = open("Inputs/2.12.txt").read().split("\n")

parsedData = []
tempData = []
for i in data:
    tempData.append(i.split(": "))

parsedData = tempData
tempData = []

for i in parsedData:
    for j in i:
        tempData.append(j.split("; "))

parsedData = tempData
tempData = []

numberRed = 12
numberGreen = 13
numberBlue = 14
sumOfPossible = 0

k = 0
while k <= len(parsedData)-2:
    l = 0
    gamePossible = True
    while l < len(parsedData[k+1]):
        m = 0
        for i in parsedData[k+1][l].split(", "):
            if i[-1] == "d":
                if int(parsedData[k+1][l].split(", ")[m][0:2]) > numberRed:
                    gamePossible = False
            if i[-1] == "n":
                if int(parsedData[k+1][l].split(", ")[m][0:2]) > numberGreen:
                    gamePossible = False
            if i[-1] == "e":
                if int(parsedData[k+1][l].split(", ")[m][0:2]) > numberBlue:
                    gamePossible = False
            m += 1
        l += 1
    if gamePossible:
        sumOfPossible = sumOfPossible + int(parsedData[k][-1][5:])
    k += 2
print(sumOfPossible)
