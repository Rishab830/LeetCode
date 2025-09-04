class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = []
        for _ in range(numRows):
            matrix.append([])
        length = len(s)
        l = 0
        row = 0
        dirc = 'up'
        while l < length:
            matrix[row].append(s[l])
            if dirc == 'up' and row < numRows - 1:
                row += 1
                if row == numRows - 1:
                    dirc = 'down'
            elif dirc == 'down' and row > 0:
                row -= 1
                if row == 0:
                    dirc = 'up'
            l += 1
        print(matrix)
        flatten = []
        for row in matrix:
            flatten += row
        return ''.join(flatten)

print(Solution().convert("PAYPALISHIRING", 3))  # "PAHNAPLSIIGYIR"
print(Solution().convert("PAYPALISHIRING", 4))  # "PYAIHRNAPLSIIG"