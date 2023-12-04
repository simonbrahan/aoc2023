import re

def scoreFromLine(line):
    cardParts = re.split(':|\|', line)

    myNumbers = numListFrom(cardParts[1])
    winningNumbers = numListFrom(cardParts[2])

    myWinners = myNumbers.intersection(winningNumbers)

    return len(myWinners)


def numListFrom(cardPart):
    return set([num for num in map(int, cardPart.split())])


with open('input.txt') as file:
    cardScores = {}
    cardCounts = {}
    for num, line in enumerate(file):
        cardScores[num+1] = scoreFromLine(line)
        cardCounts[num+1] = 1

    numCards = len(cardScores)

for cardNum in range(1, numCards+1):
    numCopies = cardCounts[cardNum]
    copyRange = cardScores[cardNum]

    for copyNum in range(cardNum+1, cardNum+copyRange+1):
        cardCounts[copyNum] += numCopies

print(sum(cardCounts.values()))
