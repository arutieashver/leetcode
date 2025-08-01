class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            elif num == 0:
                if count > max_length:
                    max_length = count
                count = 0

        if count > max_length:
                    max_length = count
                    
        return max_length

