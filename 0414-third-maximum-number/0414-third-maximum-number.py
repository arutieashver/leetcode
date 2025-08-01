class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        count = 1
        if len(set(nums)) < 3:
            return max(nums)
        elif len(nums) == 3:
            nums.sort(reverse = True)
            return (nums[-1])
        else:
            nums.sort(reverse=True)
            for i in range(len(nums)):
                if nums[i+1] != nums[i]:
                    count += 1
                if count == 3:
                    return nums[i+1]


            