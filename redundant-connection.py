class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def find(parent, i):
            if parent[i] == i:
                return i
            return find(parent, parent[i])

        def union(parent, rank, x, y):
            xroot = find(parent, x)
            yroot = find(parent, y)

            if rank[xroot] < rank[yroot]:
                parent[xroot] = yroot
            elif rank[xroot] > rank[yroot]:
                parent[yroot] = xroot
            else:
                parent[yroot] = xroot
                rank[xroot] += 1

        def findRedundantConnection(edges):
            n = len(edges)
            parent = [i for i in range(n + 1)]
            rank = [0 for i in range(n + 1)]

            for edge in edges:
                x = edge[0]
                y = edge[1]

                if find(parent, x) == find(parent, y):
                    return edge
                else:
                    union(parent, rank, x, y)
                    
        return findRedundantConnection(edges)