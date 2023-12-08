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


def startNodes(nodeMap):
    out = []
    for node in nodeMap.keys():
        if node[-1] == 'A':
            out.append(node)

    return out


def finished(nodes):
    for node in nodes:
        if node[-1] != 'Z':
            return False

    return True


def moveFromNodes(currentNodes, nodeMap, direction):
    out = []
    for currentNode in currentNodes:
        out.append(nodeMap[currentNode][direction])

    return out


directions, nodeMap = parseInput('input.txt')

currentNodes = startNodes(nodeMap)
numSteps = 0

while not finished(currentNodes):
    direction = directions[numSteps % len(directions)]
    currentNodes = moveFromNodes(currentNodes, nodeMap, direction)
    numSteps += 1

print(numSteps)
