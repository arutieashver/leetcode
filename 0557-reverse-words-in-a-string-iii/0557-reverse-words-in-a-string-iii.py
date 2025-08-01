class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        result = ''
        

        def reverse(word):
            rev = ''
            i = len(word) - 1
            while i >= 0:
                rev += word[i]
                i -= 1
        
            return rev

        for word in words:
            revword = reverse(word)
            if len(result) == len(s) - len(word):
                result = result + revword
            else:
                result = result + revword + ' '
            
        return result

        

        