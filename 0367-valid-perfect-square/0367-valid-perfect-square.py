class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0 or num == 1:
            return True
        
        left = 0
        right = num //2

        while left <= right:
            mid = (left + right) // 2
            squared = mid * mid
            if squared == num:
                return True
            elif squared < num:
                left = mid + 1
            else: 
                right = mid -1

        return False