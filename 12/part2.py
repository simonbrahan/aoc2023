def parseInput(fileName):
    with open(fileName) as file:
        return [parseLine(line) for line in file]


def parseLine(line):
    springs, damageSpec = line.strip().split()

    return (list('?'.join([springs] * 5)), list(map(int, damageSpec.split(',') * 5)))


rows = parseInput('sample.txt')

for springs, damageSpec in rows:
    print(''.join(springs), damageSpec)
