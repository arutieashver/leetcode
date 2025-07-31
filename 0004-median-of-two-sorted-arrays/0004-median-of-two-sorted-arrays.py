class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedarray = nums1 + nums2
        mergedarray.sort()
        if len(mergedarray) % 2 != 0:
            return mergedarray[int(len(mergedarray)/2)]
        else:
            i = len(mergedarray)//2
            j = i - 1
            return (mergedarray[i] + mergedarray[j])/2