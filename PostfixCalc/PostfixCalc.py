from sys import stdin

def Add(agr1, arg2):
    return agr1 + arg2

def Subtract(arg1, arg2):
    return arg1 - arg2

def Multiply(arg1, arg2):
    return arg1 * arg2

def Divide(arg1, arg2):
    if arg2 == 0:
        print("Zero division")
        return None
    return arg1 // arg2



def SomeOperator(input):
    input = input.strip()
    if input == '+':
        return Add
    if input == '-':
        return Subtract
    if input == '*':
        return Multiply
    if input == '/':
        return Divide
    return None

def EvalLine(Line):
    stack = []
    for token in Line.split():
        operation = SomeOperator(token)
        if operation != None:
            if len(stack) < 2:
                print("Malformed expression")
                return False
            arg2 = stack.pop()
            arg1 = stack.pop()
            res = operation(arg1, arg2)
            if res is None:
                return False
            stack.append(res)
        else:
            token = token.strip()
            try:
                number = int(token)
                stack.append(number)
                # expect concrete exception?
            except:
                print("Malformed expression")
                return False
    # print result
    if len(stack) != 1:
        print("Malformed expression")
        return False
    res = stack.pop()
    print(res)
    return True

def EvalAll(file):
    for line in file:
        if line.strip() == "":
            continue
        EvalLine(line)



# MAIN
# file = open("INPUT")
EvalAll(stdin)




