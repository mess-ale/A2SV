import math
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
def two():
    return([int(a) for a in input().split()])

t = inp()
for i in range(t):
    x = inp()
    bits = []
    while x >= 1:
        x = x / 2
        if x % 1 != 0:
            bits.append(1)
            x = math.floor(x)

        else:
            bits.append(0)

    ans = []
    i = 0
    while i < len(bits):
        if bits[i] == 1:
            if i-1 >= 0:
                if i < len(bits)-1:
                    ans.append(1)
                    break
                elif i == len(bits)-1:
                    ans.pop()
                    ans.insert(0,1)
                    ans.append(1)
                    break


            else:
                ans.append(1)
                if i+1 < len(bits):
                    if bits[i-1] == 1:
                        ans.append(0)
                    else:
                        ans.append(1)
                    break
                else:
                    ans.append(1)
                    break

        ans.append(0)
        i += 1
    # print(bits)
    # print(ans)
    cur = 0
    for i in range(len(ans)):
        cur += ((2 ** i) * ans[i])

    print(cur)
