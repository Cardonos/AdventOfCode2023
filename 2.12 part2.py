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

sumOfPowers = 0

k = 0
while k <= len(parsedData)-2:
    minRed = 0
    minGreen = 0
    minBlue = 0
    l = 0
    while l < len(parsedData[k+1]):
        m = 0
        for i in parsedData[k+1][l].split(", "):
            if i[-1] == "d":
                if int(parsedData[k+1][l].split(", ")[m][0:2]) > minRed:
                    minRed = int(parsedData[k+1][l].split(", ")[m][0:2])
            if i[-1] == "n":
                if int(parsedData[k+1][l].split(", ")[m][0:2]) > minGreen:
                    minGreen = int(parsedData[k+1][l].split(", ")[m][0:2])
            if i[-1] == "e":
                if int(parsedData[k+1][l].split(", ")[m][0:2]) > minBlue:
                    minBlue = int(parsedData[k+1][l].split(", ")[m][0:2])
            m += 1
        l += 1
    powerOfGame = minRed*minBlue*minGreen
    sumOfPowers = sumOfPowers + powerOfGame
    k += 2
print(sumOfPowers)
