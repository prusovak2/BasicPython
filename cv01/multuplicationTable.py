
import sys


def printLine(multiplicator, lineNumber):
    if lineNumber < 10:
        print(' ', end='')
    print(str(lineNumber), end='')
    print(" *", multiplicator, "= ", end='')
    multiple=multiplicator*lineNumber
    if multiple < 10:
        print("  ", end='')
    elif multiple < 100:
        print(" ", end='')
    print(str(multiple))


if len(sys.argv) < 2:
    print("error")
else:
    inputNum=int(sys.argv[1])
    for i in range(1, 11):
        printLine(inputNum, i)
