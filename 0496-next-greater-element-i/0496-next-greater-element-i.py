class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        for i in nums1:
            index = nums2.index(i)
            while index < len(nums2):
                if nums2[index] > i:
                    result.append(nums2[index])
                    break
                elif nums2[index] == nums2[-1]:
                    result.append(-1)
                    break
                else: 
                    index += 1
        return result
