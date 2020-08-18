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

def atan3(x1,y1,x2,y2): #1->2の角度
    return marh.atan2(y2-y1,x2-x1)

def atan3A(a1,a2): #1->2の角度
    return marh.atan2(a2[1]-a1[1],a2[0]-a1[0])
