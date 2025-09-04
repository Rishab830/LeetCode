class Stack:
    def __init__(self, n):
        self.stack = [None for _ in range(n)]
        self.pointer = 0

    def push(self, num):
        self.stack[self.pointer] = num
        self.pointer += 1

    def pop(self):
        self.pointer -= 1
        return self.stack[self.pointer]

    def peek(self):
        return self.stack[self.pointer - 1]

    def is_empty(self):
        return self.pointer == 0

class Solution:
    def isValid(self, s: str) -> bool:
        valid_dict = {'(': ')',
                      '[': ']',
                      '{': '}'}
        stack = Stack(len(s))
        for c in s:
            if c in valid_dict.keys():
                stack.push(c)
            elif valid_dict.get(stack.peek(),None) == c:
                stack.pop()
            else:
                return False
        return stack.is_empty()