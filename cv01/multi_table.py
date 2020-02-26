import sys

def multi(number):
    print('multipication table of',number)
    for i in range(11):
        print(i*number)

print(sys.argv[1])
num=int(sys.argv[1])
print('calling function with',num)
multi(num)
print('after call')
    
