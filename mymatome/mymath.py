import math
from functools import reduce

def gcd(*number):
    return reduce(math.gcd,number)

def lcm_(a,b):
    return (a*b)//gcd(a,b)

def lcm(*number):
    return reduce(lcm_,number)

def rad(d):
    return math.radians(d)

def deg(d):
    return math.degrees(d)
