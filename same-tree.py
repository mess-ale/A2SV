# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        bools = True
        def isSame(p,q):
            nonlocal bools
            if p == None or q == None:
                if p == None and q == None:
                    return True
                else:
                    bools = False
                    return False

            if p.val == q.val:
                isSame(p.left,q.left)
                isSame(p.right,q.right)
            else:
                bools = False
                return False

        isSame(p,q)
        return bools