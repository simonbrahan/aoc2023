def parseMaps(fileName):
    with open(fileName) as file:
        fileParts = file.read().split('\n\n')
        seeds = list(map(int, fileParts[0][6:].split()))

        maps = []
        for mapSpec in fileParts[1:]:
            maps.append(mapFromSpec(mapSpec))

    return seeds, maps


def mapFromSpec(spec):
    name, *mapRanges = spec.strip().split('\n')

    return (
        name[:-5],
        mapFromRanges(mapRanges)
    )


def mapFromRanges(ranges):
    out = {}
    for spec in ranges:
        destinationStart, sourceStart, rangeLength = map(int, spec.split())
        for offset in range(rangeLength):
            out[sourceStart + offset] = destinationStart + offset

    return out


def locationFor(seed, maps):
    position = seed

    for name, partialMap in maps:
        if position in partialMap:
            position = partialMap[position]

    return position


seeds, maps = parseMaps('sample.txt')

nearest = None
for seed in seeds:
    location = locationFor(seed, maps)
    if nearest == None or location < nearest:
       nearest = location

print(nearest)
