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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        for _ in range(k - 1):
            node = self.removeNode(head)
            self.pushNode(dummy_head, node)
        start = head
        head = dummy_head.next
        curr = start.next
        while True:
            temp = start
            for _ in range(k):
                temp = temp.next
                if temp is None:
                    return head
            for _ in range(k - 1):
                node = self.removeNode(curr)
                self.pushNode(start, node)
            start = curr
            curr = start.next

    def pushNode(self, prev, node):
        temp = prev.next
        prev.next = node
        node.next = temp

    def removeNode(self, prev):
        temp = prev.next
        prev.next = prev.next.next
        return temp


print(Solution().reverseKGroup(ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5))))), 3))