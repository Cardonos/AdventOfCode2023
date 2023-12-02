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
sumOfPowers = 0
k = 0
while k <= len(parsedData)-2:  # iterating over all games
    minRed = 0
    minGreen = 0
    minBlue = 0
    l = 0
    while l < len(parsedData[k+1]):  # iterating over all sets of one game
        m = 0
        for i in parsedData[k+1][l].split(", "):  # iterating over all cubes of one set  of one game
            numberOfCubes = int(parsedData[k+1][l].split(", ")[m][0:2])
            if i[-1] == "d":                    # checks if the current looked at number of cubes is higher than the
                if numberOfCubes > minRed:      # previously needed minimum number for that game and updates the
                    minRed = numberOfCubes      # minimum accordingly
            if i[-1] == "n":
                if numberOfCubes > minGreen:
                    minGreen = numberOfCubes
            if i[-1] == "e":
                if numberOfCubes > minBlue:
                    minBlue = numberOfCubes
            m += 1
        l += 1
    powerOfGame = minRed*minBlue*minGreen
    sumOfPowers = sumOfPowers + powerOfGame
    k += 2
print(sumOfPowers)
