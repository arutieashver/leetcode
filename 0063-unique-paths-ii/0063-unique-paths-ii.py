class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        prev_row = [0] * n
        k = 1
        for j in range(m-1, -1, -1):
            curr_row = [0]*n
            if obstacleGrid[j][-1] == 1:
                k = 0
            curr_row[-1] = k
        
            for i in range(n-2, -1, -1):
                curr_row[i] = (prev_row[i] + curr_row[i+1]) * (1-obstacleGrid[j][i])
            prev_row = curr_row
        return prev_row[0]