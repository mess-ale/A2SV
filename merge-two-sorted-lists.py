class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (list1 == None) & (list2 == None):
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        temp = None
        if list1.val < list2.val:
            temp = list1
            temp.next = self.mergeTwoLists(list1.next, list2)
        else:
            temp = list2
            temp.next = self.mergeTwoLists(list1, list2.next)
        
        return temp