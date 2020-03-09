import sys

def evaluate(op, arg1, arg2):
    if op == '+':
        return arg1 + arg2
    if op == '-':
        return arg1 - arg2
    if op == '*':
        return arg1 * arg2
    if op == '/':
        return arg1/arg2

def solve(stack):
    cur = stack.pop()
    print(cur)
    try:
        num = int(cur)
        return num
    except:
        arg1 = solve(stack)
        arg2 = solve(stack)
        return evaluate(cur, arg1, arg2)

print('starting')
if(len(sys.argv)<=1):
    print("missing args")

stack = []
for i in range(0, len(sys.argv)):
    stack.append(sys.argv[i])

print()
print(stack)
res = solve(stack)
print(res)
