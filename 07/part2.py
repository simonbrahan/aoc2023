import collections

def parseHands(fileName):
    out = []
    with open(fileName) as file:
        for line in file:
            handChars, bidChars = line.split()

            hand = list(handChars)
            bid = int(bidChars)
            handType = typeOf(hand)

            out.append((handType, hand, bid))

    return out


def typeOf(hand):
    cardCount = cardCountForHand(hand)

    typeCounts = [
        [1, 1, 1, 1, 1],
        [2, 1, 1, 1],
        [2, 2, 1],
        [3, 1, 1],
        [3, 2],
        [4, 1],
        [5]
    ]

    for priority, typeCount in enumerate(typeCounts):
        if cardCount == typeCount:
            return priority


def cardCountForHand(hand):
    counts = collections.Counter(hand)

    if 'J' in counts and len(counts) > 1:
        numJokers = counts['J']
        del counts['J']
    else:
        numJokers = 0

    out = sorted(counts.values(), reverse = True)
    out[0] += numJokers

    return out


def keyForHand(handInfo):
    cardScores = []
    faceMap = {
        'T': 10,
        'J': 1,
        'Q': 12,
        'K': 13,
        'A': 14
    }

    for card in handInfo[1]:
        if card in faceMap:
            cardScores.append(faceMap[card])
        else:
            cardScores.append(int(card))

    return (handInfo[0], cardScores, handInfo[2])


hands = parseHands('input.txt')

hands.sort(key = keyForHand)

winnings = 0

for rank, hand in enumerate(hands):
    winnings += hand[2] * (rank+1)

print(winnings)
