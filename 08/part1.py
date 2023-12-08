import re

def parseInput(fileName):
    with open(fileName) as file:
        instructionSpec, _, *nodeSpecs = map(lambda line: line.strip(), file.readlines())

    return list(instructionSpec), nodesFrom(nodeSpecs)


def nodesFrom(nodeSpecs):
    out = {}

    for nodeSpec in nodeSpecs:
        node, left, right, *_ = re.split('\W+', nodeSpec)
        out[node] = {'L': left, 'R': right}

    return out


directions, nodes = parseInput('input.txt')

currentNode = 'AAA'
numSteps = 0

while currentNode != 'ZZZ':
    direction = directions[numSteps % len(directions)]
    currentNode = nodes[currentNode][direction]
    numSteps += 1

print(numSteps)
