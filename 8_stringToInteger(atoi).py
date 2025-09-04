class Solution:
    def myAtoi(self, s: str) -> int:
        result = ""
        num = set("1234567890")
        s = s.strip()
        for c in s: 
            if c in  "+-" and not result:
                result += c
                continue
            if c in num:
                result += c
                continue
            break
        try:
            if int(result) > 2**31 - 1:
                return 2**31 - 1
            elif int(result) < -2**31:
                return -2**31
            return int(result) if result else 0
        except:
            return 0