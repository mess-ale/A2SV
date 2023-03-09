# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        val  = TreeNode()
        def helper(node, p, q):
            nonlocal val
            if node == None:
                return 0
                
            if p.val == node.val or q.val == node.val:
                val = node
                return node

            if p.val < node.val < q.val:
                val = node
                return node
            
            if p.val > node.val:
                helper(node.right, p, q)

            if q.val < node.val:
                helper(node.left, p, q)
                
        helper(root, TreeNode(min(p.val, q.val)), TreeNode(max(p.val, q.val)))
        return val