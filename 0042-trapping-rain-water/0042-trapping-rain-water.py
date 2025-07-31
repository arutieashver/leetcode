class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = height[0]
        right_max = height[right]
        result = 0
        
        
        while left < right:
            if left_max <= right_max:
                result += left_max - height[left]
                left += 1
                left_max = max(left_max, height[left])
            else:
                result += right_max - height[right]
                right -= 1
                right_max = max(right_max, height[right])
        return result

        