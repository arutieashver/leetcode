class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        n = rows * columns
        
        def real_index(flat_index):
            r = flat_index // columns  
            c = flat_index % columns   
            return r, c
        
        left, right = 0, n - 1
        
        while left <= right:
            mid = (left + right) // 2
            r, c = real_index(mid)
            mid_val = matrix[r][c]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False