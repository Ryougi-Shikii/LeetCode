class Solution:
    def minOperations(self, nums: list[int]) -> int:
        stair = nums
        n = len(stair)
        
        total_operations_sum = 0
        
        for i in range(1, n):
            if stair[i] < stair[i-1]:
                diff = stair[i-1] - stair[i]
                total_operations_sum += diff
                
        return total_operations_sum