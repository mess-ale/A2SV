class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = list(range(n))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
            
        for a, b in pairs:
            union(a, b)
        
        groups = {}
        for i in range(n):
            root = find(i)
            if root not in groups:
                groups[root] = []
            groups[root].append(i)
        
        res = list(s)
        for indices in groups.values():
            chars = [s[i] for i in indices]
            chars.sort()
            for i, c in zip(indices, chars):
                res[i] = c
        
        return ''.join(res)