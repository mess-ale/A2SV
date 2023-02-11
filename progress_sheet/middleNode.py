# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = head
        count = 0
        while s:
            s = s.next
            count += 1

        middel = count//2
        while middel:
            head = head.next
            middel -= 1
            
        return head
