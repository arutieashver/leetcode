class Solution:
    def fib(self, n: int) -> int:
        summation = [0,1]
        sum = 0
        
        if n == 0:
            return 0

        if n == 1:
            return 1
        

        for i in range(1,n):
            sum = summation[0] + summation[1]
            summation.pop(0)
            summation.append(sum)

        return sum
            