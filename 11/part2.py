import itertools

def parseInput(fileName):
    with open(fileName) as file:
        out = [list(line.strip()) for line in file]

    return out


def emptyRowsFrom(universe):
    out = []
    for y, row in enumerate(universe):
        if '#' not in row:
            out.append(y)

    return out

def emptyColumnsFrom(universe):
    out = []
    for x in range(len(universe[0])):
        if '#' not in column(universe, x):
            out.append(x)

    return out


def column(grid, colIdx):
    return [row[colIdx] for row in grid]


def galaxyPairsFrom(universe):
    galaxies = []
    for y, row in enumerate(universe):
        for x, tile in enumerate(row):
            if tile == '#':
                galaxies.append((x, y))

    return itertools.combinations(galaxies, 2)


def distanceBetween(pair, emptyRows, emptyColumns):
    [ax, ay], [bx, by] = pair
    expansionEffect = expansionEffectFrom(ax, bx, emptyColumns) + expansionEffectFrom(ay, by, emptyRows)

    return abs(ax-bx) + abs(ay-by) + expansionEffect


def expansionEffectFrom(start, end, empties):
    out = 0
    for place in range(min(start, end), max(start, end)+1):
        if place in empties:
            out += 999999

    return out


universe = parseInput('input.txt')
emptyRows = emptyRowsFrom(universe)
emptyColumns = emptyColumnsFrom(universe)

galaxyPairs = galaxyPairsFrom(universe)

print(sum(map(lambda pair: distanceBetween(pair, emptyRows, emptyColumns), galaxyPairs)))
