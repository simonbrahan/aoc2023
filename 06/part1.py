import math

def parseRaces(fileName):
    with open(fileName) as file:
        times, recordDistances = list(map(numsFromLine, file.readlines()))

    return list(zip(times, recordDistances))


def numsFromLine(line):
    return list(map(int, line.strip().split()[1:]))


def countWaysToWin(time, recordDistance):
    out = 0
    for i in range(time):
        if i * (time - i) > recordDistance:
            out += 1

    return out


races = parseRaces('input.txt')

numWaysToWin = []
for time, recordDistance in races:
    numWaysToWin.append(countWaysToWin(time, recordDistance))

print(math.prod(numWaysToWin))
