class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        map1 = []
        map2 = []
        for char in pattern:
            map1.append(pattern.index(char))
        for word in s:
            map2.append(s.index(word))
        return map1 == map2