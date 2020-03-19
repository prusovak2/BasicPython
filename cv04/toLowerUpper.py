import sys

if len(sys.argv) !=3:
    print("usage: toLowerUpper.py -L filename  to convert to lowercase")
    print("usage: toLowerUpper.py -U filename  to convert to uppercase")
else:
    low=False
    print(sys.argv[1])
    if sys.argv[1] == '-L':
        print('low')
        low = True
    elif sys.argv[1] != '-U':
        raise ValueError

    with open(sys.argv[2]) as file:
        for line in file:
            if(low):
                print(str.lower(line))
            else:
                print(str.upper(line))
