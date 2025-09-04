def is_palindrome(s):
        return s == s[::-1]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        l = len(s)
        while l > 0:
            start = 0
            while start + l <= length:
                if is_palindrome(s[start:start+l]):
                    return s[start:start+l]
                start += 1
            l -= 1