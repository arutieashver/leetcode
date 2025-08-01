class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        reserve = 0
        histogram = {}

        if len(s) == 1:
            return 1

        for char in s: 
            if char in histogram:
                histogram[char] += 1
            elif char not in histogram:
                histogram[char] = 1
           

        for key in histogram:
            if histogram[key] == len(s):
                return histogram[key]
            elif histogram[key] % 2 == 0:
                length += histogram[key]
            elif histogram[key] % 2 != 0:
                length += histogram[key] - 1
                reserve += 1
        
        if reserve >= 1:
            return length + 1
        else:
            return length