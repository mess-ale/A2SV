class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        graph = defaultdict(set)
        for i in roads:
            graph[i[0]].add(i[1])
            graph[i[1]].add(i[0])
        
        ans = 0
        for i in graph:
            for j in graph:
                if i != j:
                    if j in graph[i]:
                        ans = max(ans, len(graph[i])+len(graph[j])-1)
                    else:
                        ans = max(ans, len(graph[i])+len(graph[j]))

        return ans