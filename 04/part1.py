import re

def scoreFromLine(line):
    cardParts = re.split(':|\|', line)
    myNumbers = numListFrom(cardParts[1])
    winningNumbers = numListFrom(cardParts[2])

    myWinners = myNumbers.intersection(winningNumbers)

    if len(myWinners) == 0:
        return 0

    return 2**(len(myWinners)-1)


def numListFrom(cardPart):
    return set([num for num in map(int, cardPart.split())])


with open('input.txt') as file:
    print(sum(scoreFromLine(line) for line in file))
