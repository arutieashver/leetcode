class Solution:
    def convertToBase7(self, num: int) -> str:
        result = ""
        if num == 0:
            return '0'

        if num < 0:
            sign = '-'
        else:
            sign = ''
        
        num = abs(num)
        
        while num:
            result = str(num % 7) + result
            num //= 7
        return sign + result

        