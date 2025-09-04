from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_dict = {'2': 'abc',
                    '3': 'def',
                    '4': 'ghi',
                    '5': 'jkl',
                    '6': 'mno',
                    '7': 'pqrs',
                    '8': 'tuv',
                    '9': 'wxyz',
                    }
        if not digits:
            return []
        ans = ['']
        for n in digits:
            new_ans = []
            for e in ans:
                for l in num_dict[n]:
                    new_ans.append(e+l)
            ans = new_ans
        return ans