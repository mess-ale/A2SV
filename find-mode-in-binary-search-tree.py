# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        dec = defaultdict(int)
        def helper(node):
            nonlocal dec
            if node == None:
                return None
            helper(node.left)
            dec[node.val] += 1
            helper(node.right)

        helper(root)
        stack = []
        decs = sorted(dec.items(), key=lambda x:x[-1])
        print(decs)
        for i in range(len(decs)-1,-1,-1):
            if i == len(decs)-1:
                stack.append(decs[i][0])

            else:
                if decs[i+1][1] == decs[i][1]:
                    stack.append(decs[i][0])
                else:
                    break

        return stack