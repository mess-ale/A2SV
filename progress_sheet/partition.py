# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return head
        lis = []
        while head:
            lis.append(head.val)
            head = head.next
            
        les = []
        i = 0
        while i < len(lis):
            if lis[i] < x:
                les.append(lis[i])
                del lis[i]
            else:
                i+=1
                
        su = les+lis
        dummy = ListNode(10)
        m = ListNode(su[0])
        dummy.next = m
        for j in range(1,len(su)):
            m.next = ListNode(su[j])
            m = m.next
        return dummy.next
