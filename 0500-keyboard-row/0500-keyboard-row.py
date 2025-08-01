class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result = []
        row1 = ['q','w','e','r','t','y','u','i','o','p']
        row2 = ['a','s','d','f','g','h','j','k','l']
        row3 = ['z','x','c','v','b','n','m']

        def inRow(word, row):
            temp = word.lower()
            for letter in temp:
                if letter in row:
                    continue
                if letter not in row:
                    return False
            return True

        for word in words:
            if inRow(word, row1):
                result.append(word)
            if inRow(word, row2):
                result.append(word)
            if inRow(word, row3):
                result.append(word)
        
        return result