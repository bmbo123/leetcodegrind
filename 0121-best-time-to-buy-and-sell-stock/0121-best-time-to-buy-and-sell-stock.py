class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        m = prices[0]
        for i in range(1,len(prices)):
            m = min(m, prices[i])
            maxP = max(maxP, prices[i] - m)
        return maxP
            

            