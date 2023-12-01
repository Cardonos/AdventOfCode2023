data = open("Inputs/1.12.txt").read().split("\n")

output = []
for i in data:
    newLine = i
    lineFinished = False
    while not lineFinished:
        currLine = newLine
        newLine = ""
        if "one" in currLine:
            a = currLine.find("one")
            newLine = currLine[0:a] + "o1e" + currLine[a + 3:len(currLine)]
        elif "two" in currLine:
            a = currLine.find("two")
            newLine = currLine[0:a] + "t2o" + currLine[a + 3:len(currLine)]
        elif "three" in currLine:
            a = currLine.find("three")
            newLine = currLine[0:a] + "t3e" + currLine[a + 5:len(currLine)]
        elif "four" in currLine:
            a = currLine.find("four")
            newLine = currLine[0:a] + "f4r" + currLine[a + 4:len(currLine)]
        elif "five" in currLine:
            a = currLine.find("five")
            newLine = currLine[0:a] + "f5e" + currLine[a + 4:len(currLine)]
        elif "six" in currLine:
            a = currLine.find("six")
            newLine = currLine[0:a] + "s6x" + currLine[a + 3:len(currLine)]
        elif "seven" in currLine:
            a = currLine.find("seven")
            newLine = currLine[0:a] + "s7n" + currLine[a + 5:len(currLine)]
        elif "eight" in currLine:
            a = currLine.find("eight")
            newLine = currLine[0:a] + "e8t" + currLine[a + 5:len(currLine)]
        elif "nine" in currLine:
            a = currLine.find("nine")
            newLine = currLine[0:a] + "n9e" + currLine[a + 4:len(currLine)]
        else:
            lineFinished = True
            output.append(currLine)

finalSum = 0
for i in output:
    digOne = 0
    digTwo = 0
    j = 0
    while j <= (len(i) + 1):
        try:
            digOne = digOne + int(i[j])
            break
        except:
            j += 1
    j = 0
    while j <= (len(i) + 1):
        try:
            digTwo = digTwo + int(i[(len(i) + 1) - j])
            break
        except:
            j += 1
    fullNum = int(str(digOne) + str(digTwo))
    finalSum = finalSum + fullNum
print(finalSum)
