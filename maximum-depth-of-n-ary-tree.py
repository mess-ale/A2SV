"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        def dfs(root):
            if root == None:
                return 0
            if root.children == None:
                return 1

            depth = 0
            for i in root.children:
                depth = max(depth, dfs(i))
                
            return depth+1

        return dfs(root)