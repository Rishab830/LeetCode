class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self.next:
            return f"{self.val} -> {self.next.__repr__()}"
        return f"{self.val}"
    
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        new_head = None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            new_head = list1 
            curr1 = curr1.next
        else:
            new_head = list2
            curr2 = curr2.next
        new_curr = new_head
        while curr1 is not None and curr2 is not None:
            if curr1.val < curr2.val:
                new_curr.next = curr1
                curr1 = curr1.next
                new_curr = new_curr.next
            else:
                new_curr.next = curr2
                repr(new_curr)
                curr2 = curr2.next
                new_curr = new_curr.next
        if curr1 is not None:
            new_curr.next = curr1
        else:
            new_curr.next = curr2
        return new_head