import re
data = open("Inputs/1.12.txt").read().split("\n")

decodeResult ={
    "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "one": 1, "tw": 2, "wo": 2, "thre": 3, "hree": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eigh": 8, "ight": 8, "nine": 9,
}

j = 0
Summe = 0
parsedData = []

for i in data:
    result = re.findall(r"\d|one|tw|wo|thre|hree|four|five|six|seven|eigh|ight|nine", data[j])
    parsedData.append(result)
    j += 1

for i in parsedData:
    twoDigit = (str(decodeResult[i[0]]) + str(decodeResult[i[-1]]))
    Summe = Summe + int(twoDigit)
print(Summe)


