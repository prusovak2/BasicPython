import sys

if(len(sys.argv)!=2):
    print('incorect amount of args')
else:    
    hight=int(sys.argv[1])
    stars=1
    for i in range(0,hight):
        for j in range(0,hight-i):
            print(' ',end='')
        for j in range(0,stars):
            print('*',end='')
        print()
        stars+=2
    for i in range(0,hight):
        print(' ',end='')
    print('*')
