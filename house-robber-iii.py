# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def trivers(root):
            if root:
                left = trivers(root.left)
                right = trivers(root.right)
                return [max(root.val+left[1]+right[1], left[0]+right[0]), left[0]+right[0]]
            else:
                return [0, 0]

        val = trivers(root)
        return max(val)