class Solution:
    def isHappy(self, n: int) -> bool:
        values = []
    
        while n != 1:
            values.append(n)
            digits = [int(digit) for digit in str(n)]
            for digit in digits:
                digits[digits.index(digit)] = digit ** 2
            n = sum(digits)
            if n in values:
                return False

        return True
