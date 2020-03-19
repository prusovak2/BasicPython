import sys

if len(sys.argv) < 2:
    print('incorrect usage')
else:
    counter = 0
    with open(sys.argv[1]) as inputFile:
        for line in inputFile:
            for word in line.split():
                print(word)
                counter+=1
                print(counter)
        print()
        print(counter)
                
