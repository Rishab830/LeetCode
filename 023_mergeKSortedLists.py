class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self.next:
            return f"{self.val} -> {self.next.__repr__()}"
        return f"{self.val}"

from typing import Optional

class Heap:
    def __init__(self, arr):
        self.arr = arr
        for i in range(len(arr) // 2 - 1, -1, -1):
            self._heapify_top_down(i)

    def heapify(self):
        self._heapify_top_down(0)

    def _heapify_top_down(self, i):
        minimum = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < len(self.arr) and self.arr[minimum].val > self.arr[l].val:
            minimum = l
        if r < len(self.arr) and self.arr[minimum].val > self.arr[r].val:
            minimum = r
        if minimum != i:
            self.arr[i], self.arr[minimum] = self.arr[minimum], self.arr[i]
            self._heapify_top_down(minimum)

    def _heapify_bottom_up(self, i):
        parent = (i - 1) // 2
        if parent >= 0 and self.arr[parent] > self.arr[i]:
            self.arr[parent], self.arr[i] = self.arr[i], self.arr[parent]
            self._heapify_bottom_up(parent)

    def peek(self):
        return self.arr[0] if self.arr else None

    def pop(self):
        temp = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop(-1)
        self._heapify_top_down(0)
        return temp

    def push(self, val):
        self.arr.append(val)
        self._heapify_bottom_up(len(self.arr) - 1)

    def __repr__(self):
        return f"Heap({self.arr})"

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        for li in lists.copy():
            if not li:
                lists.remove(li)
        if not lists:
            return None
        heap = Heap(lists)
        head_ans = heap.peek()
        ans = head_ans
        heap.arr[0] = heap.peek().next
        if heap.arr[0] is None:
            heap.pop()
        heap.heapify()
        while heap.peek():
            ans.next = heap.peek()
            ans = ans.next
            heap.arr[0] = heap.peek().next
            if heap.arr[0] is None:
                heap.pop()
            heap.heapify()
            print(ans.val)
        return head_ans