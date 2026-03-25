class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def f(amt, ind):
            if (ind,amt) in dp: return dp[(ind,amt)]
            if ind>=len(coins):
                return 10**5
            
            if amt==0:
                return 0

            skip=f(amt,ind+1)
            take=10**5
            if amt>=coins[ind]:
                take=1+f(amt-coins[ind],ind)
            dp[(ind, amt)] =min(skip,take)
            return dp[(ind,amt)]
        dp=dict()
        ans= f(amount,0)
        if ans>amount:
            return -1
        return ans
        