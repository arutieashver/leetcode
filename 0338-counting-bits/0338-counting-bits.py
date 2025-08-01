class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        
        def oneCount(n):
            count = 0
            while n > 0:
                count += n & 1   # Add 1 if the least significant bit (rightmost bit) is 1
                n = n >> 1       # Shift bits right by 1 to check the next bit
            return count

        for n in range(0, n + 1):
            value = oneCount(n)
            result.append(value)

        return result