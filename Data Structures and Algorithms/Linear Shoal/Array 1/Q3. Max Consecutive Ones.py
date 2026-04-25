class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur = 0
        best = 0
        for i in nums:
            if i:
                cur+=1
            else:
                best = max(best, cur)
                cur = 0
        return max(best, cur)