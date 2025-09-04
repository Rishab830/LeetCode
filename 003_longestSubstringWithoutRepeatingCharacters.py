class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        set_length = len(set(s))
        l = set_length
        while l > 0:
            start = 0
            while start < length-l+1:
                if len(set(s[start:start+l])) == l:
                    return l
                start += 1
            l -= 1
        return 0