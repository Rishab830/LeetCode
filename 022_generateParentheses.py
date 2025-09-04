# 1: ()
# 2: (()), ()()
# 3: ((())), (()()), (())(), 
# 4: (((()))), ((()())), ((())()), (()(())), (()()()), (())()(), ()(())(), ()()(()), (()())(), ()(()()), ()()()()

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def rec_gen(string, left, right, n):
            if left == right and right == n:
                ans.append(string)
                return
            if left == right:
                rec_gen(string + '(', left + 1, right, n)
                return
            if left > right and left != n:
                rec_gen(string + '(', left + 1, right, n)
                rec_gen(string + ')', left, right + 1, n)
                return
            if left > right and left == n:
                rec_gen(string + ')', left, right + 1, n)
                return
        rec_gen('', 0, 0, n)
        return ans
    
print(Solution().generateParenthesis(3))