class Solution(object):
    def maxRotateFunction(self, nums):
         n = len(nums)
         total_sum = sum(nums)  # Calculate the sum of all elements in the array
        
         current_sum = sum(i * nums[i] for i in range(n))  # Calculate the initial value of F(0)
         max_sum = current_sum
        
         # Iterate through the array starting from index 1 to n-1
         for i in range(1, n):
            current_sum += total_sum - n * nums[n-i]  # Calculate the new value of F(i)
            max_sum = max(max_sum, current_sum)  # Update the max_sum variable if necessary
            
         return max_sum