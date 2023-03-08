# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        vals = TreeNode(-10)
        def serch(node, number):
            nonlocal vals
            if node == None:
                return None
            elif node.val == number:
                vals = node
                return None
            elif node.val > number:
                serch(node.left, number)
            elif node.val < number:
                serch(node.right, number)
        serch(root, val)
        if vals.val == -10:
            return None
        return vals