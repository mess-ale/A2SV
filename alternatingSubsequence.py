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

t = inp()
for i in range(t):
    n = inp()
    lis = inlt()
    ans = []
    i = 0
    j = 1
    while j <= len(lis):
        if j == len(lis):
            ans.append(max(lis[i:j]))
            break

        elif lis[i] > 0 and lis[j] > 0:
            j += 1

        elif lis[i] < 0 and lis[j] < 0:
            j += 1

        else:
            ans.append(max(lis[i:j]))
            i = j
            j += 1

    print(sum(ans))
