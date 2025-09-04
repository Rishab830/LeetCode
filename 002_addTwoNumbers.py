class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self.next:
            return f"{self.val} -> {self.next.__repr__()}"
        return f"{self.val}"

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l3 = ListNode()
        l1_node = l1
        l2_node = l2
        l3_node = l3
        carry = 0
        sum_node = l1.val + l2.val
        print(sum_node)
        if sum_node < 10:
            l3.val = sum_node
        else:
            l3.val = sum_node % 10
            carry = 1
        while l1_node.next is not None and l2_node.next is not None:
            node_sum = l1_node.next.val + l2_node.next.val + carry
            print(node_sum)
            if node_sum < 10:
                l3_node.next = ListNode(val=node_sum)
                carry = 0
            else:
                l3_node.next=ListNode(val=node_sum%10)
                carry = 1
            l1_node = l1_node.next
            l2_node = l2_node.next
            l3_node = l3_node.next
        print("out")
        if l1_node.next is not None:
            print("l1 left out")
            while l1_node.next is not None:
                node_sum = l1_node.next.val + carry
                print(node_sum)
                if node_sum < 10:
                    l3_node.next = ListNode(val=node_sum)
                    carry = 0
                else:
                    l3_node.next = ListNode(val=node_sum%10)
                    carry = 1
                l1_node = l1_node.next
                l3_node = l3_node.next
        if l2_node.next is not None:
            print("l2 left out")
            while l2_node.next is not None:
                node_sum = l2_node.next.val + carry
                print(node_sum)
                if node_sum < 10:
                    l3_node.next = ListNode(val=node_sum)
                    carry = 0
                else:
                    l3_node.next = ListNode(val=node_sum%10)
                    carry = 1
                l2_node = l2_node.next
                l3_node = l3_node.next
        if carry == 1:
            l3_node.next = ListNode(val=1)
        return l3