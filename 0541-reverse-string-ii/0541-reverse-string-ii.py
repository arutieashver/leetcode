class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(s):
            i = len(s) - 1
            rev = ''
            while i >= 0:
                rev += s[i]
                i -= 1
            return rev

        result = ''
        segments = [s[i:i+k] for i in range(0, len(s), k)]
        flip = True

        for segment in segments:
            if flip:
                result += reverse(segment)
                flip = False
            else:
                result += segment
                flip = True

        return result
            

                

