# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ave = []
        def avedec(node):
            nonlocal ave
            if node == None:
                return None
            avedec(node.left)
            ave.append(node.val)
            avedec(node.right)

        counter = 0
        def helper(node):
            nonlocal ave
            nonlocal counter
            if node == None:
                return None

            helper(node.left)
            avedec(node)
            if sum(ave)//len(ave) == node.val:
                counter += 1
            ave = []
            helper(node.right)

        helper(root)
        return counter