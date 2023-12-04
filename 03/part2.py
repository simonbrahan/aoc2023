import math

def parseSchematic(fileName):
    numbers = {}
    gears = []
    with open(fileName) as file:
        for y, line in enumerate(file):
            lineNumbers, lineGears = parseLine(line, y)
            numbers[y] = lineNumbers
            gears += lineGears

    return numbers, gears


def parseLine(line, y):
    numbers = []
    gears = []

    currentDigits = []
    for x, char in enumerate(line):
        if char.isdigit():
            currentDigits.append(char)
            continue

        if len(currentDigits) > 0:
            numbers.append(
                {
                    'number': int(''.join(currentDigits)),
                    'start': x-len(currentDigits),
                    'end': x-1,
                }
            )

            currentDigits = []

        if char == '*':
            gears.append((x, y))

    if len(currentDigits) > 0:
        numbers.append(
            {
                'number': int(''.join(currentDigits)),
                'start': x-len(currentDigits),
                'end': x-1,
            }
        )

    return numbers, gears


def ratioFor(gear, numbers):
    adjacentSpaces = adjacentSpacesFor(gear)

    considerNumbers = []
    for y in range(gear[1]-1, gear[1]+2):
        if y in numbers:
            considerNumbers += numbers[y]

    gearNumbers = numbersIn(adjacentSpaces, considerNumbers)

    if len(gearNumbers) == 2:
        return math.prod(gearNumbers)

    return 0


def adjacentSpacesFor(coordinate):
    transforms = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    startX, startY = coordinate

    return set([(startX + x, startY + y) for x, y in transforms])


def numbersIn(spaces, numbers):
    out = []
    for number in numbers:
        if numberInSpaces(number, spaces):
            out.append(number['number'])

    return out


def numberInSpaces(number, spaces):
    for x, y in spaces:
        if number['start'] <= x and number['end'] >= x:
            return True

    return False


numbers, gears = parseSchematic('input.txt')

gearRatioSum = 0

for gear in gears:
    gearRatioSum += ratioFor(gear, numbers)

print(gearRatioSum)
