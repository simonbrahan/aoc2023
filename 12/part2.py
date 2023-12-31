import functools
import re

def parseInput(fileName):
    with open(fileName) as file:
        return [parseLine(line) for line in file]


def parseLine(line):
    springs, damageSpec = line.strip().split()

    return ('?'.join([springs] * 5), tuple(map(int, damageSpec.split(',') * 5)))


@functools.cache
def countPossibleArrangements(springs, damageSpec):
    # No more damage groups...
    if len(damageSpec) == 0:
        # and no more damaged springs - valid
        if '#' not in springs:
            return 1
        # still some damaged springs - invalid
        else:
            return 0

    # More damage groups, but no more springs - invalid
    if len(springs) == 0:
        return 0

    # Ignore healthy springs
    if springs[0] == '.':
        return countPossibleArrangements(springs[1:], damageSpec)

    if springs[0] == '?':
        withOkSpring = countPossibleArrangements('.' + springs[1:], damageSpec)
        withBrokeSpring = countPossibleArrangements('#' + springs[1:], damageSpec)
        return withOkSpring + withBrokeSpring

    #
    # Looking at a broken spring
    #

    nextGroupSize = damageSpec[0]

    # Not enough remaining springs to satisfy group
    if len(springs) < nextGroupSize:
        return 0

    # There is an ok spring within the group
    if re.search(r'\.', springs[:nextGroupSize]):
        return 0

    # The group is larger than specified
    if len(springs) > nextGroupSize and springs[nextGroupSize] == '#':
        return 0

    # Skip the group and the next spring, since that one must be ok
    return countPossibleArrangements(springs[nextGroupSize+1:], damageSpec[1:])


rows = parseInput('input.txt')

numPossibleArrangements = 0
for springs, damageSpec in rows:
    numPossibleArrangements += countPossibleArrangements(springs, damageSpec)

print(numPossibleArrangements)
