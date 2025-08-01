class Solution:
    def firstUniqChar(self, s: str) -> int:
        histogram = {}

        for char in s:
            if char in histogram:
                histogram[char] += 1
            else:
                histogram[char] = 1

        for key in histogram:
            if histogram[key] == 1:
                return s.index(key)
            
        return -1

