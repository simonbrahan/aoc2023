import operator

def parseInput(fileName):
    with open(fileName) as file:
        return [list(line.strip()) for line in file]


def tiltNorth(platform):
    for y, row in enumerate(platform):
        for x, cell in enumerate(row):
            if cell != 'O':
                continue

            rollNorth(platform, x, y)

    return platform


def rollNorth(platform, x, y):
    if y == 0:
        return

    rollDistance = 0
    while y - rollDistance > 0:
        if platform[y-rollDistance-1][x] != '.':
            break

        rollDistance += 1

    if rollDistance == 0:
        return

    platform[y - rollDistance][x] = 'O'
    platform[y][x] = '.'


def checkLoad(platform):
    out = 0
    maxLoad = len(platform)
    for y, row in enumerate(platform):
        out += operator.countOf(row, 'O') * (maxLoad - y)

    return out


platform = parseInput('input.txt')

tiltedNorth = tiltNorth(platform)

print(checkLoad(platform))
