# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        lis = []
        while head:
            lis.append(head.val)
            head = head.next

        i = 0
        j = 1
        count = 0
        while j < len(lis):
            if lis[i] == lis[j]:
                del lis[j]
                count += 1
            else:
                if count > 0:
                    count = 0
                    del lis[i]
                else:
                    i += 1
                    j += 1
        if count > 0:
            del lis[-1]
        dammy = ListNode(10)
        if len(lis) == 0:
            return dammy.next
        
        dammy = ListNode(10)
        s = ListNode(lis[0])
        dammy.next = s
        new = s
        for i in range(1,len(lis)):
            s = new
            new = ListNode(lis[i])
            s.next = new
            
        return dammy.next

