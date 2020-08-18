import random

def randI(a,b):
    return random.randint(a,b)

def randD(a,b):
    return random.uniform(a,b)

def randIs(a,b,l):
    return [randI(a,b) for i in range(l)]

def randDs(a,b,l):
    return [randD(a,b) for i in range(l)]
