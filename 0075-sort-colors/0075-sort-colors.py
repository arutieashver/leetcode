class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first = 0 
        last = len(nums) - 1
        curr = 0
        while curr <= last:
            if nums[curr] == 0:
                nums[first], nums[curr] = nums[curr], nums[first]
                first += 1
                curr += 1
            elif nums[curr] == 1:
                curr += 1
            else:
                nums[curr], nums[last] = nums[last], nums[curr]
                last -= 1