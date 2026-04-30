class Solution:
    def fib(self, n: int) -> int:
        memo = dict()
        memo[0] = 0
        memo[1] = 1
        memo[2] = 1
        def dp(n):
            if n in memo:
                return memo[n]
            v = dp(n-1) + dp(n-2)
            memo[n] = v
            return memo[n]
        return dp(n)