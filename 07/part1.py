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
    cardCount = sorted(collections.Counter(hand).values(), reverse = True)

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


def keyForHand(hand):
    cardScores = []
    faceMap = {
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }

    for card in hand[1]:
        if card in faceMap:
            cardScores.append(faceMap[card])
        else:
            cardScores.append(int(card))

    return (hand[0], cardScores, hand[2])


hands = parseHands('input.txt')

hands.sort(key = keyForHand)

winnings = 0

for rank, hand in enumerate(hands):
    winnings += hand[2] * (rank+1)

print(winnings)
