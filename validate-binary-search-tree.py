# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        prev = []
        def helper(node):
            nonlocal prev
            if node == None:
                return 0
            helper(node.left)
            prev.append(node.val)
            helper(node.right)
        
        helper(root)
        s = sorted(list(set(prev)))
        if prev == s:
            return True

        return False