class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        intersection = ''
        i = 0
        j = 0

        ransomNote = ''.join(sorted(ransomNote))
        magazine = ''.join(sorted(magazine))


        while i < len(ransomNote) and j < len(magazine):
            if ransomNote[i] < magazine[j]:
                i += 1
            elif ransomNote[i] > magazine[j]:
                j += 1
            else: 
                intersection += ransomNote[i]
                i += 1
                j += 1
        
        return intersection == ransomNote
        
            