# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ls = []
        while head:
            ls.append(head.val)
            head = head.next

        i = 0
        j = len(ls)-1
        maxi = 0
        while i < j:
            maxi = max(maxi, ls[i]+ls[j])
            i += 1
            j -= 1

        return maxi