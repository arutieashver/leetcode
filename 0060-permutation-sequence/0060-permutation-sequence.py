class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n+1)] 
        factorial = [1] * n
        for i in range(1, n):
            factorial[i] = factorial[i-1] * i
        
        k -= 1
        result = [] 
        for i in range(n-1, -1, -1):
            index = k // factorial[i]
            result.append(str(nums[index]))
            nums.pop(index)
            k = k % factorial[i]
        
        return ''.join(result)