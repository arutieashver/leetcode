class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = list(accumulate(grid[0]))
        for i in range(1, len(grid)):
            for j in range(len(dp)):
                    dp[j] = grid[i][j] + (dp[j] if j == 0 else min(dp[j], dp[j-1]))
        return dp[-1]