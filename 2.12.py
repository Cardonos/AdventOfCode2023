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
numberRed = 12
numberGreen = 13
numberBlue = 14
sumOfPossible = 0

k = 0
while k <= len(parsedData)-2:  # iterating over all games
    l = 0
    gamePossible = True
    while l < len(parsedData[k+1]) and gamePossible:  # iterating over all sets of one game as long as its possible
        m = 0
        for i in parsedData[k+1][l].split(", "):  # iterating over all cubes of one set of one game
            numberOfCubes = int(parsedData[k+1][l].split(", ")[m][0:2])  # reads out the number of cubes of the current
            if i[-1] == "d":  # checks if the color is red               # looked at color
                if numberOfCubes > numberRed:
                    gamePossible = False
                    break
            if i[-1] == "n":  # checks if the color is green
                if numberOfCubes > numberGreen:
                    gamePossible = False
                    break
            if i[-1] == "e":  # checks if the color is blue
                if numberOfCubes > numberBlue:
                    gamePossible = False
            m += 1
        l += 1
    if gamePossible:
        sumOfPossible = sumOfPossible + int(parsedData[k][-1][5:])  # adds the current game id onto the sum
    k += 2
print(sumOfPossible)
