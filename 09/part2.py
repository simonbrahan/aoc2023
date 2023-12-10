def parseInput(fileName):
    out = []
    with open(fileName) as file:
        for line in file:
            out.append(list(map(int, line.split())))

    return out


def nextValueOf(history):
    if numbersAllMatch(history):
        return history[0]

    valueDiffs = diffsBetween(history)

    return history[0] - nextValueOf(valueDiffs)


def numbersAllMatch(numbers):
    return all(num == numbers[0] for num in numbers)


def diffsBetween(nums):
    numCount = len(nums)
    if numCount < 2:
        return []

    out = []
    for idx in range(numCount - 1):
        out.append(nums[idx+1] - nums[idx])

    return out


histories = parseInput('input.txt')

sumOfNextValues = 0
for history in histories:
    sumOfNextValues += nextValueOf(history)

print(sumOfNextValues)
