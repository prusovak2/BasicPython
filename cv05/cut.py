import  sys
import pandas as pd
import getopt

def usage():
    print('cut.py –d delimiter –f columns to be printed')

def determineFields(stringFields):
    if ',' in stringFields:
        fields = stringFields.split(',')
        intFields = []
        for item in fields:
            intFields.append(int(item))
        return intFields
    if '-' in stringFields:
        fields = stringFields.split('-')
        if stringFields.startswith('-'):
            intFields = range(1, int(fields[1])+1)
            return intFields
        if stringFields.endswith('-'):
            intFields = ['end', int(fields[0])]
            return intFields
        intFields = range(int(fields[0]), int(fields[1])+1)
        return intFields
    intFields = [int(stringFields[0])]
    return intFields



try:
    opts, args = getopt.getopt(sys.argv[1:], 'd:f:', ['delim, fields'])
except getopt.GetoptError:
    usage()
    sys.exit(2)

for opt, arg in opts:
    if opt in ('-d', '--delim'):
        delim=arg
    elif opt in ('-f', '--fields'):
        fields = arg
    else:
        usage()
        sys.exit(2)

fieldsArr = determineFields(fields)
for i in fieldsArr:
    print(i)
print()
for line in sys.stdin:
    saveArray = fieldsArr
    splited = line.split(delim)
    if saveArray[0] == 'end':
        fieldsArr = range(fieldsArr[1], len(splited)+1)
    for i in fieldsArr:
        if (i > 0) & (i <= len(splited)):
            #print(i, len(splited))
            print(splited[i-1], end='\t')
    print()
