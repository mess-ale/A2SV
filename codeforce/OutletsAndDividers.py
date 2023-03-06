
fir = list(map(int, input().split()))
name_list = list(map(int, input().split()))

prefix_sum = [0]
cur = 0
for i in name_list:
    if i <= fir[2]:
        cur += i
        prefix_sum.append(cur)

start = 0
ans = 0
index = 0
while index < len(prefix_sum):
    if prefix_sum[index]-prefix_sum[start] <= fir[2]:
        index += 1

    else:
        if fir[1] <= prefix_sum[index-1]-prefix_sum[start] <= fir[2]:
            ans += 1
            start = index-1
            
print(ans)

