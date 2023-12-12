def parseInput(fileName):
    with open(fileName) as file:
        return [parseLine(line) for line in file]


def parseLine(line):
    springs, damageSpec = line.strip().split()

    return (list(springs), list(map(int, damageSpec.split(','))))


def countPossibleArrangements(springs, damageSpec):
    candidateArrangements = getCandidateArrangements(springs)

    out = 0
    for candidate in candidateArrangements:
        if isValid(candidate, damageSpec):
            out += 1

    return out


def isValid(springs, damageSpec):
    damageGroups = getDamagedGroups(springs)
    return damageGroups == damageSpec


def getDamagedGroups(springs):
    out = []
    currentCount = 0
    for spring in springs:
        if spring == '#':
            currentCount += 1
            continue

        if currentCount > 0:
            out.append(currentCount)
            currentCount = 0

    if currentCount > 0:
        out.append(currentCount)

    return out


def getCandidateArrangements(springs):
    if '?' not in springs:
        return [springs]

    optIdx = springs.index('?')

    withOkSpring = [springs[:optIdx] + ['.'] + opt for opt in getCandidateArrangements(springs[optIdx+1:])]
    withBrokeSpring = [springs[:optIdx] + ['#'] + opt for opt in getCandidateArrangements(springs[optIdx+1:])]

    return withOkSpring + withBrokeSpring


rows = parseInput('input.txt')

numPossibleArrangements = 0
for springs, damageSpec in rows:
    numPossibleArrangements += countPossibleArrangements(springs, damageSpec)

print(numPossibleArrangements)
