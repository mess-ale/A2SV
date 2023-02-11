# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        lists = []
        while head:
            lists.append(head.val)
            head = head.next
        
        val = k%len(lists)
        new = []
        i = 0
        j = len(lists)-1
        while val > 0:
            new.append(lists[j])
            del lists[j]
            j -= 1
            val -= 1
        ss = new[::-1]
        ss.extend(lists)
        dummy = ListNode(10)
        s = ListNode(ss[0])
        dummy.next = s
        for i in range(1,len(ss)):
            s.next = ListNode(ss[i]) 
            s = s.next
        return dummy.next
