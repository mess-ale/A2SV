# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
lists = []
n = int(input())
for i in range(n):
    lists.append(input())
dic = Counter(lists)
print(len(dic))
for key in dic:
    print(dic.get(key),end=" ")
