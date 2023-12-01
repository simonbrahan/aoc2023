def calibrationFromLine(line):
    firstDigit = None
    lastDigit = None
    idx = 0
    while True:
        idx, char = nextDigit(line, idx)

        if char == None:
            break

        lastDigit = char

        if firstDigit == None:
            firstDigit = char

    return int(firstDigit + lastDigit)


def nextDigit(line, startIdx):
    digits = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    for idx in range(startIdx, len(line)):
        considerChars = line[idx:]
        if considerChars[0].isdigit():
            return idx+1, considerChars[0]

        for word, digit in digits.items():
            if considerChars.startswith(word):
                return idx+1, digit

    return None, None


with open('input.txt') as file:
    out = 0
    for line in file:
        out += calibrationFromLine(line)

print(out)
