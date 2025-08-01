class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        prev = 1
        for i in range(1, rowIndex + 1):
            next_val = prev * (rowIndex - i + 1) // i
            result.append(next_val)
            prev = next_val
        return result