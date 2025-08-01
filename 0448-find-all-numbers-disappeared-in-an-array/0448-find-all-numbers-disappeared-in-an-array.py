class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        check = set([num for num in range(1,len(nums) + 1)])
        nums = set(nums)

        disappearednums = check.difference(nums)
        result = list(disappearednums)
        return result 