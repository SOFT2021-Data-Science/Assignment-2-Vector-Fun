import numpy as n
import math

def mag(vec):
    x = vec[0]
    y = vec[1]
    
    return math.sqrt(x**2 + y**2)


def unit(vec):
    x = vec[0]
    y = vec[1]
    m = mag(vec)
    
    return n.array([x/m, y/m])

def rot90(vec):
    x = vec[0]
    y = vec[1]
    
    return n.array([-y, x])


a = n.array([3, 2])
b = n.array([8, 7])
c = n.array([1, 5])
a90 = rot90(a)

print(2*a)
print(a+b-c)
print(n.dot(a, a))
print(mag(a)*mag(a))
print(n.dot(a, b))
print(mag(a)*mag(b))
print(n.dot(a, a90))



