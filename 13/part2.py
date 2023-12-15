def parseInput(fileName):
    with open(fileName) as file:
        patternChunks = file.read().split('\n\n')

    out = []
    for patternChunk in patternChunks:
        out.append([list(line.strip()) for line in patternChunk.split()])

    return out


def scoreReflections(pattern):
    for y in range(len(pattern)):
        if reflectsAcrossHorizontal(pattern, y):
            return 100 * (y + 1)

    for x in range(len(pattern[0])):
        if reflectsAcrossVertical(pattern, x):
            return x + 1


def reflectsAcrossHorizontal(pattern, y):
    if y > len(pattern) - 2:
        return False

    offset = 0
    foundSmudge = False
    while y - offset >= 0 and y + offset + 1 < len(pattern):
        a = pattern[y - offset]
        b = pattern[y + offset + 1]

        for aTile, bTile in zip(a, b):
            if aTile != bTile:
                if foundSmudge:
                    return False

                foundSmudge = True

        offset += 1

    return foundSmudge


def reflectsAcrossVertical(pattern, x):
    if x > len(pattern[0]) - 2:
        return False

    offset = 0
    foundSmudge = False
    while x - offset >= 0 and x + offset + 1 < len(pattern[0]):
        a = column(pattern, x - offset)
        b = column(pattern, x + offset + 1)

        for aTile, bTile in zip(a, b):
            if aTile != bTile:
                if foundSmudge:
                    return False

                foundSmudge = True

        offset += 1

    return foundSmudge


def column(pattern, x):
    return [row[x] for row in pattern]


patterns = parseInput('input.txt')

totalScore = 0
for pattern in patterns:
    totalScore += scoreReflections(pattern)

print(totalScore)
