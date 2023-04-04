import math
 
def inp():
    return(int(input()))
def invr():
    return(input())
def inlt():
    return(list(map(int,input().split())))
def two():
    return([int(a) for a in input().split()])
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
 
a, b = two()
if a == b:
    print(a)
 
else:
    print(1)
