# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        s = left
        if head.next is None:
            return head
            
        demmy = ListNode(10)
        demmy.next = head
        def reverslenkedlist(firstlist,right,left):
            prev = None
            curs = firstlist
            while curs and right-left+1:
                temp = curs.next
                curs.next = prev
                prev = curs
                curs = temp
                right -= 1
            return prev, curs

        cur = demmy
        while cur and left-1:
            cur = cur.next
            left -= 1

        last = cur.next
        prev,curs = reverslenkedlist(cur.next,right,s)
        cur.next = prev
        last.next = curs
        return demmy.next

