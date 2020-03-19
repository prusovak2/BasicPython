import sys

def countWords():
    if len(sys.argv) < 2:
        print('incorrect usage')
    else:
        counter = 0
        with open(sys.argv[1]) as inputFile:
            for line in inputFile:
                for word in line.split():
                    print(word)
                    counter += 1
                    print(counter)
            print()
            print(counter)

def allignAndPrint(inputFile, outputFile, numChars):
    charCounter = 0
    linetobe = ''
    for line in inputFile:
        for word in line.split():
            if charCounter+len(word) > numChars:
                print(linetobe, file=outputFile)
                linetobe = ''
                charCounter = 0
            linetobe += (word + ' ')
            charCounter += len(word) +1
        if linetobe != '':
            print(linetobe, file=outputFile)


if (len(sys.argv) < 3) | (len(sys.argv) >= 5):
    print('incorrect usage', len(sys.argv))
else:
    with open(sys.argv[1]) as inputFile:
        numChars = int(sys.argv[2])
        if len(sys.argv) == 4:
            with open(sys.argv[3], mode="w") as outputFile:
                allignAndPrint(inputFile, outputFile, numChars)
        else:
            allignAndPrint(inputFile, sys.stdout, numChars)
