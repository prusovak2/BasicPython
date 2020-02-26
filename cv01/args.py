import sys

def args_fak():
    for i in range(len(sys.argv)-1, 0, -1):
        print(sys.argv[i])

args_fak()
