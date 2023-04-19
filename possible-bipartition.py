class Solution:
    def possibleBipartition(self, n: int, dislikes) -> bool:
        graph = [[] for _ in range(n)]
        for a, b in dislikes:
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)
        colors = [0] * n
        def dfs(node, color):
            colors[node] = color
            for neighbor in graph[node]:
                if colors[neighbor] == color:
                    return False
                if colors[neighbor] == 0 and not dfs(neighbor, -color):
                    return False
            return True
        for i in range(n):
            if colors[i] == 0 and not dfs(i, 1):
                return False
        return True