from collections import defaultdict


n = int(input())
graph = defaultdict(list)
for i in range(n):
    ls = list(map(int, input().split()))
    for j in range(len(ls)):
        if ls[j] == 1:
            graph[i+1].append(j+1)

visited = set()
for j in graph:
    for i in graph[j]:
        temp = str(i)+str(j) if i < j else str(j)+str(i)
        if temp not in visited:
            visited.add(temp)
            
print(len(visited))
