class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]

        n = len(nums)
        first = -1
        last = -1

        # Find first occurrence
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                first = mid
                high = mid - 1  # continue searching in left half
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        # Find last occurrence
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                last = mid
                low = mid + 1  # continue searching in right half
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return [first, last]