n = int(input())
k = int(input())

# Initialize adjacency list
adj_list = [[] for _ in range(n)]

for i in range(k):
    op, u, *v = map(int, input().split())

    if op == 1:
        # Add edge (u, v)
        v = v[0]
        adj_list[u-1].append(v-1)
        adj_list[v-1].append(u-1)
    else:
        # Print adjacent vertices of u
        neighbors = adj_list[u-1]
        print(" ".join(str(x+1) for x in neighbors) if neighbors else "")
