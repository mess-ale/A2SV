class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        visited = set()
        def dfs(graph, vertex):     
            nonlocal visited
            
            visited.add(vertex)
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    dfs(graph, neighbour)
                graph[neighbour] = []
                
        graph = defaultdict(list)
        for i in edges:
            graph[i[0]].append(i[1])

        for i in range(n):
            if i not in visited:
                dfs(graph, i)
                
        ans = [x for x in graph if graph[x]]
        return ans