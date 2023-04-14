"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        lis = {}
        total = 0
        for i in employees:
            lis[i.id] = (i.importance, i.subordinates)

        def dfs(node):
            nonlocal total
            total += node[0]
            for i in node[1]:
                dfs(lis[i])

        dfs(lis[id])
        return total