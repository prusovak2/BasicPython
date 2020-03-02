import sys

if len(sys.argv) < 2:
    print("error")
else:
    input = sys.argv[1]
    splitted = input.split('/')
    lenght = len(splitted)
    for i in range(lenght-1):
        print(splitted[i])
    if '.' in splitted[lenght-1]:
        last = splitted[lenght-1].split('.')
        print(last[0])
        print(last[1])
    else:
        print(splitted[lenght-1])


