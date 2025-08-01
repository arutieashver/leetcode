class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = nums.count(0)
        
        for x in range(0,z):
            nums.remove(0)
            nums.append(0)
