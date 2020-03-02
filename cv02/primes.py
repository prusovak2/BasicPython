import sys

if len(sys.argv) < 3:
    print("error")
else:
    first = int(sys.argv[1])
    second = int(sys.argv[2])
    if first > second:
        tmp = first
        first = second
        second = tmp

    myList = list(range(second+1))
    for i in range(2, second+1):
        for j in range(i, second+1):
            toRemove = i*j
            try:
                myList.remove(toRemove)
            except:
                pass

    primes = 0
    for i in range(2,len(myList)):
        if(myList[i]>=first and myList[i]<=second):
            primes += 1
            print(myList[i])

    print()
    print(primes)


