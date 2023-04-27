# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        qe = deque()
        qe.append(root)

        while qe:
            le = len(qe)
            temp = []
            for i in qe:
                if i:
                    temp.append(i.val)
                
            for i in range(le):
                if qe[0]:
                    qe.append(qe[0].left)
                    qe.append(qe[0].right)
                qe.popleft()
            if temp:
                ans.append(sum(temp)/len(temp))
                
        return ans