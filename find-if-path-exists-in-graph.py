class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = list(range(n))
        rank = [0]*n
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx == rooty:
                return

            if rank[rootx] < rank[rooty]:
                rootx, rooty = rooty, rootx

            parent[rooty] = rootx
            if rank[rootx] == rank[rooty]:
                rank[rootx] += 1

        def connected(x, y):
            return find(x) == find(y)

        for i, j in edges:
            union(i, j)

        return connected(source, destination)