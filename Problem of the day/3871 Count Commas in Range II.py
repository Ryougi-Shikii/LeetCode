class Solution:
    def countCommas(self, n: int) -> int:
        def helper(n, threshold):
            if threshold > n:
                return 0
            
            return (n - threshold + 1) + helper(n, threshold * 1000)
        
        return helper(n, 1000)