class Solution:
    def rob(self, nums: List[int]) -> int:
        # f(i) = max(f(i+1), nums[i] + f(i+2))
        
        n = len(nums)
        ans = {}

        def rec(i):
            if i >= n:
                return 0

            if i in ans:
                return ans[i]

            skip = rec(i + 1)
            take = nums[i] + rec(i + 2)

            ans[i] = max(skip, take)
            return ans[i]

        return rec(0)