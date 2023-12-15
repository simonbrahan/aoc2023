import re

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


tests = [
    ('', (), 1),
    ('?', (), 1),
    ('.', (), 1),
    ('.?', (), 1),
    ('#', (), 0),
    ('', (1,), 0),
    ('.', (1,), 0),
    ('#', (1,), 1),
    ('.#', (1,), 1),
    ('#.', (1,), 1),
    ('##', (2,), 1),
    ('#', (2,), 0),
    ('#.', (2,), 0),
    ('###', (2, 1), 0),
    ('#.#', (1, 1), 1),
    ('##.#', (2, 1), 1),
    ('?', (1,), 1),
    ('.?', (1,), 1),
    ('?.', (1,), 1),
    ('??', (2,), 1),
    ('??', (1,), 2),
    ('???', (3,), 1),
    ('???', (2,), 2),
    ('???', (1, 1), 1),
    ('???.###', (1, 1, 3), 1),
    ('.??..??...?##.', (1, 1, 3), 4),
    ('?#?#?#?#?#?#?#?', (1, 3, 1, 6), 1),
    ('????.#...#...', (4, 1, 1), 1),
    ('????.######..#####.', (1, 6, 5), 4),
    ('?###????????', (3, 2, 1), 10),
]

for springs, damageSpec, expect in tests:
    actual = countPossibleArrangements(springs, damageSpec)
    if actual != expect:
        print('test', springs, '-', damageSpec, 'returned ', actual, ': ', expect, 'expected')

