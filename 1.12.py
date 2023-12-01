import re

data = open("Inputs/1.12.txt").read().split("\n")

j = 0
Summe = 0
for i in data:
    result = re.findall(r"\d", data[j])
    twoDigit = (result[0]+result[-1])
    Summe = Summe + int(twoDigit)
    j += 1
print(Summe)
