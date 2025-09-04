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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        temp = head
        head = head.next
        temp.next = head.next
        head.next = temp
        curr = head.next
        while curr is not None and curr.next is not None and curr.next.next is not None:
            temp = curr
            curr = curr.next
            temp.next = curr.next
            curr.next = curr.next.next
            temp.next.next = curr
        return head