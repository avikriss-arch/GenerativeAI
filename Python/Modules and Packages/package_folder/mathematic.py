def add(a,b):
    return a+b

def sub(a,b):
    if a>b:
        return a-b
    else:
        return b-a

def mul(a,b):
    return a*b

def div(a,b):
    if b==0:
        print("Enter valid denominator, it should not be zero")
    else:
        return a/b