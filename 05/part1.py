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
    out = []
    for spec in ranges:
        destinationStart, sourceStart, rangeLength = map(int, spec.split())
        # Begin tuple with source start for easy sorting
        out.append((sourceStart, destinationStart, rangeLength))

    out.sort()

    return out


def locationFor(seed, maps):
    position = seed

    for name, partialMaps in maps:
        position = mapPositionFor(position, partialMaps)

    return position


def mapPositionFor(position, partialMaps):
    for sourceStart, destinationStart, rangeLength in partialMaps:
        if position < sourceStart:
            continue

        if position >= sourceStart + rangeLength:
            continue

        position = position - sourceStart + destinationStart
        break

    return position


seeds, maps = parseMaps('input.txt')

nearest = None
for seed in seeds:
    location = locationFor(seed, maps)
    if nearest == None or location < nearest:
       nearest = location

print(nearest)
