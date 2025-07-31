class Solution:
    def convert(self, s: str, numrows: int) -> str:
        if numrows == 1 or numrows >= len(s):
            return s

        rows = [''] * numrows
        current_row = 0
        going_down = False

        for i in s:
            rows[current_row] += i
            if current_row == 0 or current_row == numrows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1

        return ''.join(rows)
        