class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        nums = []
        for row in grid:
            nums.extend(row)
        
        nums.sort()
        
        anchor_remainder = nums[0] % x
        for val in nums:
            if val % x != anchor_remainder:
                return -1
        
        median = nums[len(nums) // 2]
        
        total_ops = 0
        for val in nums:
            total_ops += abs(val - median) // x
            
        return total_ops
        