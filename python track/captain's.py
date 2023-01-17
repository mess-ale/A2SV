# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter


k = int(input())
d = list(map(int, input().split()))

dic = Counter(d)
for i in dic:
    if dic[i] == 1:
        print(i)
        break
