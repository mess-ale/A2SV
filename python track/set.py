# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

n, m = list(map(int, input().split()))
main = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

ans = 0
for i in main:
    if i in A:
        ans += 1
    if i in B:
        ans -= 1
print(ans)
