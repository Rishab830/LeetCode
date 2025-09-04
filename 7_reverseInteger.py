class Solution:
    def reverse(self, x: int) -> int:
        flag = None
        flag = x < 0
        x = -x if flag else x
        y = 0
        while x != 0:
            if y * 10 + x % 10 > 2**31 - 1 or y * 10 + x % 10 < -2**31:
                print(y)
                return 0
            y = y * 10 + x % 10
            x /= 10
            x = int(x)
            print(x, y)
        return -y if flag else y