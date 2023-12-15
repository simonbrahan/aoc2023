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

    # Try options for a broke spring and an ok spring
    if springs[0] == '?':
        brokeSpringCount = countPossibleArrangements('#' + springs[1:], damageSpec)
        okSpringCount = countPossibleArrangements('.' + springs[1:], damageSpec)
        return okSpringCount + brokeSpringCount

    #
    # Looking at a broken spring
    #

    nextGroupSize = damageSpec[0]

    # Not enough remaining springs to satisfy group
    if len(springs) < nextGroupSize:
        return 0

    # There is an ok spring within the group
    if not re.match(r'^[\?#]+$', springs[:nextGroupSize]):
        return 0

    # The group is not terminated by the end of the spring row, nor by an ok spring
    if len(springs) != nextGroupSize and springs[nextGroupSize] == '#':
        return 0

    return countPossibleArrangements(springs[nextGroupSize:], damageSpec[1:])


rows = parseInput('sample.txt')

numPossibleArrangements = 0
for springs, damageSpec in rows:
    numPossibleArrangements += countPossibleArrangements(springs, damageSpec)

print(numPossibleArrangements)
