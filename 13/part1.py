def parseInput(fileName):
    with open(fileName) as file:
        patternChunks = file.read().split('\n\n')

    out = []
    for patternChunk in patternChunks:
        out.append([list(line.strip()) for line in patternChunk.split()])

    return out


def scoreReflections(pattern):
    out = 0

    for y in range(len(pattern)):
        if reflectsAcrossHorizontal(pattern, y):
            out += 100 * (y + 1)
            break

    for x in range(len(pattern[0])):
        if reflectsAcrossVertical(pattern, x):
            out += x + 1
            break

    return out


def reflectsAcrossHorizontal(pattern, y):
    if y > len(pattern) - 2:
        return False

    offset = 0
    while y - offset >= 0 and y + offset + 1 < len(pattern):
        a = pattern[y - offset]
        b = pattern[y + offset + 1]

        if a != b:
            return False;

        offset += 1

    return True


def reflectsAcrossVertical(pattern, x):
    if x > len(pattern[0]) - 2:
        return False

    offset = 0
    while x - offset >= 0 and x + offset + 1 < len(pattern[0]):
        a = column(pattern, x - offset)
        b = column(pattern, x + offset + 1)

        if a != b:
            return False;

        offset += 1

    return True


def column(pattern, x):
    return [row[x] for row in pattern]


patterns = parseInput('input.txt')

totalScore = 0
for pattern in patterns:
    totalScore += scoreReflections(pattern)

print(totalScore)
