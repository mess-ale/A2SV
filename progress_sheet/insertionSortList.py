# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sro = []
        while head:
            sro.append(head.val)
            head = head.next

        sro.sort()
        dammy = ListNode(10)
        s = ListNode(sro[0])
        dammy.next = s
        new = s
        for i in range(1,len(sro)):
            s = new
            new = ListNode(sro[i])
            s.next = new
            
        return dammy.next
