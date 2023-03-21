# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    
        def traverse(node, row, result):
            if node != None:
                if len(result) < row+1:
                    result.append([])
                result[row].append(node.val)
                traverse(node.left, row+1, result)
                traverse(node.right, row+1, result)
        
        result = []
        if root != None:
            traverse(root, 0, result)
        return result