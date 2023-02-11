# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even = []
        odd = []
        count=0
        temp = head
        while head:
            if count%2==0:
                odd.append(head.val)
            else:
                even.append(head.val)
            head = head.next
            count+=1
        if len(odd)+len(even) < 2:   
            return temp
        dummy = ListNode(10)
        s = ListNode(odd[0])
        dummy.next = s
        for i in range(1,len(odd)):
            s.next = ListNode(odd[i])
            s = s.next
            
        s.next = ListNode(even[0])
        for i in range(len(even)):
            s.next = ListNode(even[i])
            s = s.next
        return dummy.next
