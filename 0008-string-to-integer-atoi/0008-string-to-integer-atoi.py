class Solution:
    def myAtoi(self, s: str) -> int:
        max = 2**31 -1
        min = -2**31
        sign = 1
        result = 0

        if not s: 
            return 0

        #Skip leading whitespace
        s = s.lstrip()
        
        if not s: 
            return 0

        #Check for optional sign
        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        #Skip leading zeros
        s = s.lstrip("0")

        if not s:
            return 0

        #Check if remaining values are digits
        if s.isnumeric():
            result = int(s)
        else:
            subs = ''
            for item in s:
                if item.isnumeric():
                    subs += item
                else:
                    break

            if subs:
                result = int(subs)

        
        result = sign * result
        
        #Rounding
        if result < min:
            result = min
        if result > max:
            result = max

        return result