class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        totalSum = sum(nums)
        n = len(nums)
        m = n//2
        halfSum = 0
        for i in range(n//2):
            halfSum += nums[i]

        goodRotation = 0
        for i in range(n):
            if halfSum > totalSum-halfSum:
                goodRotation += 1
            halfSum = halfSum + nums[(i+m)%n] - nums[i]
        
        return goodRotation