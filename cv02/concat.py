import sys

if len(sys.argv) < 2:
    print("error")
else:
    inputNum = sys.argv[1]
    n1=int(3*inputNum)
    n2=int(2*inputNum)
    n3=int(inputNum)
    print(n1+n2+n3)

