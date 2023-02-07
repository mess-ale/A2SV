# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []
        while l1:
            list1.append(str(l1.val))
            l1 = l1.next 
        while l2:
            list2.append(str(l2.val))
            l2 = l2.next 

        s = str(int("".join(list1[::-1]))+int("".join(list2[::-1])))
        
        dummy = ListNode(5)
        test = dummy
        i = len(s)-1
        while i > -1:
            test.next = ListNode(s[i])
            test = test.next
            i -= 1
        return dummy.next
