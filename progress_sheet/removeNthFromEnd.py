# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp = head
        nodes = head
        count = 0
        while temp:
            count += 1
            temp = temp.next
            
        value = count-n
        if value != 0:
            while nodes and value:
                if value==1 and nodes.next:
                    nodes.next = nodes.next.next
                    break
                nodes = nodes.next
                value -= 1
            return head
            
        return head.next
            
