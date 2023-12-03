import re

def parseGames(fileName):
    out = []
    with open(fileName) as file:
        for line in file:
            gameParts = re.split(r';|:\s', line)
            game = {
                'id': int(gameParts[0].split(' ')[1]),
                'hands': []
            }

            for hand in gameParts[1:]:
                parsedHand = {'red': 0, 'green': 0, 'blue': 0}
                cubeCounts = re.split(',\s', hand.strip())

                for cubeCount in cubeCounts:
                    count, colour = cubeCount.split(' ')
                    parsedHand[colour] += int(count)

                game['hands'].append(parsedHand)

            out.append(game)

    return out


def gamePossible(game):
    bagContents = {'red': 12, 'green': 13, 'blue': 14}

    for hand in game['hands']:
        for colour, count in hand.items():
            if count > bagContents[colour]:
                return False

    return True


games = parseGames('input.txt')

possibleGameIds = []

for game in games:
    if gamePossible(game):
        possibleGameIds.append(game['id'])

print(sum(possibleGameIds))
