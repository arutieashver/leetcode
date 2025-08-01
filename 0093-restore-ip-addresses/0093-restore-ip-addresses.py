class Solution:
    def numPossible(self, s, i, dots, combs):
        if dots==0:
            if int(s[i:])<=255 and not (s[i]=='0' and i<len(s)-1):
                self.output.append(combs+s[i:])
            return 
        if i>=len(s)-1:
            return
        
        self.numPossible(s, i+1, dots-1, combs+s[i:i+1]+'.')
        if i == len(s) - 2 or s[i]=='0':
            return
        
        self.numPossible(s, i+2, dots-1, combs+s[i:i+2]+'.')

        if i == len(s) - 3 or int(s[i:i+3]) > 255:
            return
        
        self.numPossible(s, i+3, dots-1, combs + s[i:i+3] + '.')

        return
        
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n < 4 or n > 15:
            return []
        self.output = []
        self.numPossible(s, 0, 3, '')
        return self.output
        