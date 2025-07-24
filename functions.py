def sqrt(a):
    return int(a**(1/2))

def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    if b == 0:
        print("This operation can't be solved (Undefined)")
    elif a == 0:
        print("This operation equals 0")
    else:
        return a/b



