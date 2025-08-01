class Solution:
    def reverseVowels(self, s: str) -> str:
        result = ''
        s = [char for char in s]
        vowels = ['a','e','i','o','u','A','E','I','O','U']

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] not in vowels and s[right] not in vowels:
                left += 1
                right -= 1
            elif s[left] in vowels and s[right] not in vowels:
                right -= 1
            elif s[left] not in vowels and s[right] in vowels:
                left += 1
            elif s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        for char in s:
            result += char
        
        return result