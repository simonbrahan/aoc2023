def parseMaps(fileName):
    with open(fileName) as file:
        fileParts = file.read().split('\n\n')
        seedRanges = seedRangesFromLine(fileParts[0])

        maps = []
        for mapSpec in fileParts[1:]:
            maps.append(mapFromSpec(mapSpec))

    return seedRanges, maps


def seedRangesFromLine(line):
    nums = list(map(int, line[6:].split()))
    ranges = [tuple(nums[i:i+2]) for i in range(0, len(nums), 2)]

    return mergeRanges(ranges)


def mergeRanges(ranges):
    out = []

    currentStart = None
    currentEnd = None
    for start, length in sorted(ranges):
        if currentStart == None:
            currentStart = start
            currentEnd = start + length - 1
            continue

        if start > currentEnd:
            out.append((currentStart, currentEnd))
            currentStart = start
            currentEnd = start + length - 1
            continue

        currentEnd = start + length

    if currentStart != None:
        out.append((currentStart, currentEnd))

    return out


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


seedRanges, maps = parseMaps('input.txt')

nearest = None
for rangeStart, rangeEnd in seedRanges:
    for seed in range(rangeStart, rangeEnd+1):
        location = locationFor(seed, maps)
        if nearest == None or location < nearest:
            nearest = location

print(nearest)
