class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1 = list(num1)
        l2 = list(num2)
        n1 = 0
        n2 = 0
        a = 1
        for i in range(len(num1)-1,-1,-1):
            n1 = n1 + ((ord(l1[i])-48)*a)
            a = a*10
        a = 1
        for i in range(len(num2)-1,-1,-1):
            n2 = n2+((ord(l2[i])-48)*a)
            a = a*10
        return str(n1*n2)    