def parseInput(fileName):
    with open(fileName) as file:
        return [parseLine(line) for line in file]


def parseLine(line):
    springs, damageSpec = line.strip().split()

    return (list('?'.join([springs] * 5)), list(map(int, damageSpec.split(',') * 5)))


def countPossibleArrangements(springs, damageSpec):
    return 0


rows = parseInput('sample.txt')

numPossibleArrangements = 0
for springs, damageSpec in rows:
    numPossibleArrangements += countPossibleArrangements(springs, damageSpec)

print(numPossibleArrangements)
