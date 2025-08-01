class Solution:
    def checkRecord(self, s: str) -> bool:
        acount = 0
        lcount = 0

        for char in s:
            if char == 'P':
                lcount = 0
                continue
            if char == 'A':
                acount += 1
                lcount = 0
                if acount == 2:
                    return False
            if char == 'L':
                lcount += 1
                if lcount == 3:
                    return False

        
        return True
