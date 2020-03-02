import sys


def perm(pref, s):
    if(len(s)) == 1:
        print(pref+s)
    else:
        for i in range(len(s)):
            c = s[i]
            perm(pref+c, s[:i] + s[i+1:])


if len(sys.argv) < 2:
    print("error")
else:
    string = sys.argv[1]
    prf=''
    perm(prf, string)
