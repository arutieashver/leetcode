class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []

        def check(x,y):
            if x == y:
                result.append(str(x))   
            else:
                result.append(str(x) + '->' + str(y))

        if not nums:
            return result

        start = nums[0]
        end = nums [0]

        for n in nums[1:]:
            if n == end + 1:
                end = n
            elif n != end + 1:
                check(start,end)
                start = n
                end = n   
        
        check(start,end)
        
        return result