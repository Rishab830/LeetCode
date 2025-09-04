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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        n_prev = head
        curr = head
        while curr is not None:
            curr = curr.next
            if n == -1:
                n_prev = n_prev.next
            else:
                n -= 1
        if n != -1:
            head = head.next
            return head
        if n_prev.next is None:
            return None
        else:
            n_prev.next = n_prev.next.next
        return head