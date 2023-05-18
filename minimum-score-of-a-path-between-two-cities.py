class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [0]*n
        mini = float("inf")

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y, des):
            rootx = find(x)
            rooty = find(y)
            if rootx == rooty:
                return

            if rank[rootx] < rank[rooty]:
                rootx, rooty = rooty, rootx

            parent[rooty] = rootx
            if rank[rootx] == rank[rooty]:
                rank[rootx] += 1

        def check(x, y, des):
            nonlocal mini
            rootx = find(x)
            rooty = find(y)
            if rootx == find(1-1) or find(n-1) == rooty:
                mini = min(mini, des)
                

        for ix, iy, des in roads:
            union(ix-1, iy-1, des)

        for iix, iiy, dess in roads:
            check(iix-1, iiy-1, dess)

        return mini