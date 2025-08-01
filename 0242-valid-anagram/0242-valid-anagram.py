class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        histogram = {}

        for char in s:
            histogram[char] = s.count(char)

        for letter in t:
            if letter not in histogram:
                return False
            elif letter in histogram and histogram[letter] != t.count(letter):
                return False
            else:
                continue

        return True