class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        if n <= 2:
            return nums
        
        valid_indices = {0, n - 1}
        
        current_max = nums[0]
        for i in range(1, n - 1):
            if nums[i] > current_max:
                valid_indices.add(i)
                current_max = nums[i]
                
        current_max = nums[n - 1]
        for i in range(n - 2, 0, -1):
            if nums[i] > current_max:
                valid_indices.add(i)
                current_max = nums[i]
                
        return [nums[i] for i in range(n) if i in valid_indices]