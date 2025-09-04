from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        i = 0
        flag = False
        while True:
            if i > len(strs[0]) - 1:
                break
            c = strs[0][i]
            for word in strs:
                if i > len(word) - 1 or word[i] != c:
                    flag = True
                    break
            if flag:
                break
            prefix += c
            i += 1
        return prefix