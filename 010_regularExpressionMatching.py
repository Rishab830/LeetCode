import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern = re.compile(rf"^{p}$")
        match = pattern.match(s)
        return match is not None
            
        