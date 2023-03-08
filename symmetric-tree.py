# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        bools = True
        def check(lnode, rnode):
            nonlocal bools
            if lnode==None or rnode==None:
                if lnode==None and rnode==None:
                    return True
                else:
                    bools = False
                    return False

            if lnode.val == rnode.val:
                check(lnode.left, rnode.right)
                check(lnode.right, rnode.left)

            else:
                bools = False
                return 0

        check(root.left, root.right)
        return bools