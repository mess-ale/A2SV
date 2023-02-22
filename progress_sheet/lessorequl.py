n = list(map(int, input().split()))
nf = list(map(int, input().split()))
nf.sort()
count = 0
temp = nf[n[1]-1]
if n[1] > len(nf):
    print(-1)
elif n[1] == 0:
    if nf[0] > 1:
        print(nf[0]-1)
    else:
        print(-1)
else:
    for i in range(n[0]):
        if nf[i] <= temp:
            count += 1
    if count == n[1]:
        print(temp)
    else:
        print("-1")
