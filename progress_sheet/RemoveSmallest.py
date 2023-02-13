N = int(input())
for i in range(N):
    n = int(input())
    lis = list(map(int, input().split()))
    lis.sort()
    while 1 < n:
        if abs(lis[0]-lis[1]) <= 1:
            if lis[0]-lis[1] < 0:
                del lis[0]
            else:
                del lis[1]
        else:
            break
        n -= 1
 
    if len(lis) == 1:
        print("YES")
    else:
        print("NO")
