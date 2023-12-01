def calibrationFromLine(line):
    firstDigit = None
    lastDigit = None
    for char in line:
        if not char.isdigit():
            continue

        lastDigit = char

        if firstDigit == None:
            firstDigit = char

    return int(firstDigit + lastDigit)


with open('input.txt') as file:
    out = 0
    for line in file:
        out += calibrationFromLine(line)

print(out)
