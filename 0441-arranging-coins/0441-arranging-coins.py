class Solution:
    def arrangeCoins(self, n: int) -> int:
        sum = 0
        
        if n == 0:
            return n

        for i in range(0, n+1):
            sum += i
            if sum > n:
                return i - 1
            if sum == n:
                return i
