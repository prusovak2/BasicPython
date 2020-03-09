import sys

def selectSort(toSort):
    for i in range(0, len(toSort)):
        myMin = toSort[i]
        minIndex=i
        for j in range(i+1, len(toSort)):
            if toSort[j] < myMin:
                myMin = toSort[j]
                minIndex =j
        if minIndex != i:
            temp = toSort[i]
            toSort[i] = toSort[minIndex]
            toSort[minIndex] = temp
    return toSort

if len(sys.argv)<=1:
    print("missing args")
else:
    toSort =[]
    for i in range(1, len(sys.argv)):
        toSort.append(int(sys.argv[i]))
    sorted = selectSort(toSort)
    print(sorted)

