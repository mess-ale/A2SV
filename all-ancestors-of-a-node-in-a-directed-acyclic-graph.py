class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        indegre = [0]*n
        graph = defaultdict(list)
        for i,val in enumerate(edges):
            graph[val[1]].append(val[0])
            indegre[val[0]] += 1
            
        result = [[]]*n
        def dfs(node):
            for child in graph[node]:
                if child not in visited:
                    visited.append(child)
                    dfs(child)
                    
       
        for i in range(n):
            visited = []
            dfs(i)
            visited.sort()
            result[i] = visited

        return result