class Solution:
    def romanToInt(self, s: str) -> int:
        val = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
        }
        num = 0
        i = 0
        while i < len(s):
            if i != len(s) - 1 and val[s[i]] < val[s[i + 1]]:
                num += val[s[i + 1]] - val[s[i]]
                i += 2
            else:
                num += val[s[i]]
                i += 1
        return num