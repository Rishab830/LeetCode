class Solution:
    def isPalindrome(self, x: int) -> bool:
        og_x = x
        if x < 0:
            return False
        y = 0
        while x != 0:
            y = y * 10 + x % 10
            x //= 10
        print(y)
        return y == og_x