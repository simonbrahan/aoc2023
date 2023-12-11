import itertools

def parseInput(fileName):
    with open(fileName) as file:
        out = [list(line.strip()) for line in file]

    return out


def expand(universe):
    out = []
    for row in universe:
        out.append(row)
        if '#' not in row:
            out.append(row[:])

    universeWidth = len(out[0])

    for colIdx in range(universeWidth-1, -1, -1):
        if '#' not in column(out, colIdx):
            addColumnAfter(out, colIdx)

    return out


def column(grid, colIdx):
    return [row[colIdx] for row in grid]


def addColumnAfter(grid, colIdx):
    for row in grid:
        row.insert(colIdx+1, '.')


def galaxyPairsFrom(universe):
    galaxies = []
    for y, row in enumerate(universe):
        for x, tile in enumerate(row):
            if tile == '#':
                galaxies.append((x, y))

    return itertools.combinations(galaxies, 2)


def distanceBetween(pair):
    [ax, ay], [bx, by] = pair
    return abs(ax-bx) + abs(ay-by)


universe = parseInput('input.txt')

expandedUniverse = expand(universe)

galaxyPairs = galaxyPairsFrom(expandedUniverse)

print(sum(map(distanceBetween, galaxyPairs)))
