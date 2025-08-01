class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)

        for n in range(length+1):
            if n not in nums:
                return n