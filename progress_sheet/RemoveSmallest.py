N = int(input())
for i in range(N):
    n = int(input())
    lis = list(map(int, input().split()))
    lis.sort()
    i = 0
    j = 1
    while j < n:
        if abs(lis[i]-lis[j]) <= 1:
            if lis[i]-lis[j] < 0:
                del lis[i]
            else:
                del lis[j]
        else:
            break
        n -= 1
 
    if len(lis) == 1:
        print("YES")
    else:
        print("NO")
