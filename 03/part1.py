def parseSchematic(fileName):
    numbers = []
    symbols = set()
    with open(fileName) as file:
        for y, line in enumerate(file):
            lineNumbers, lineSymbols = parseLine(line.strip(), y)
            numbers += lineNumbers
            symbols.update(lineSymbols)

    return numbers, symbols


def parseLine(line, y):
    numbers = []
    symbols = set()

    currentDigits = []
    for idx, char in enumerate(line):
        if char.isdigit():
            currentDigits.append(char)
            continue

        if len(currentDigits) > 0:
            numbers.append(
                {
                    'number': int(''.join(currentDigits)),
                    'start': (idx-len(currentDigits), y),
                }
            )

            currentDigits = []

        if char != '.':
            symbols.add((idx, y))

    if len(currentDigits) > 0:
        numbers.append(
            {
                'number': int(''.join(currentDigits)),
                'start': (idx-len(currentDigits), y),
            }
        )

    return numbers, symbols


def isPartNumber(number, symbols):
    for space in adjacentSpaces(number):
        if space in symbols:
            return True

    return False


def adjacentSpaces(number):
    length = len(str(number['number']))
    startX, startY = number['start']
    above = [(x, startY-1) for x in range(startX-1, startX+length+1)]
    left = [(startX-1, startY)]
    right = [(startX+length, startY)]
    below = [(x, startY+1) for x in range(startX-1, startX+length+1)]

    return above + below + left + right


numbers, symbols = parseSchematic('input.txt')

partNumbers = []
for number in numbers:
    if isPartNumber(number, symbols):
        partNumbers.append(number['number'])

print(sum(partNumbers))
