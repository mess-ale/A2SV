class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        viseted = set()
        def helper(node, graph, des):
            if node == des:
                return True

            viseted.add(node)
            for child in graph[node]:
                if child not in viseted:
                    if helper(child, graph, des):
                        return True

            return False

        graph = defaultdict(list)
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])

        if helper(source, graph, destination):
            return True
        return False