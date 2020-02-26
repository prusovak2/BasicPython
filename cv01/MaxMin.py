import sys

if(len(sys.argv)>=1):
    max=int(sys.argv[1])
    min=int(sys.argv[1])
else:
    print('too few args')
for i in range(2,len(sys.argv)):
    if(max<int(sys.argv[i])):
        max=int(sys.argv[i])
    if(min>int(sys.argv[i])):
        min=int(sys.argv[i])
print('min',min)
print('max',max)
    
