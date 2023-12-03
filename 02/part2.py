import math
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


def gamePower(game):
    minColourCounts = {'red': 0, 'green': 0, 'blue': 0}
    for hand in game['hands']:
        for colour, count in hand.items():
            if minColourCounts[colour] < count:
                minColourCounts[colour] = count

    return math.prod(minColourCounts.values())


games = parseGames('input.txt')

print(sum(gamePower(game) for game in games))
