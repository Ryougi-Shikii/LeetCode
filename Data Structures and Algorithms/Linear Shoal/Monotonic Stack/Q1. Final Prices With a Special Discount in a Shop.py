class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = [0] * len(prices)
        for i in range(len(prices)):

            for j in range(i+1, len(prices)):

                if prices[i]>=prices[j]:
                    res[i] = prices[i] - prices[j]
                    break
            else:
                res[i] = prices[i]
        return res