class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0]*(len(prices))
        dp[0] = 0
        
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                dp[i] = prices[i] - prices[i-1] + dp[i-1]
            else:
                dp[i] = dp[i-1]


        return dp[-1]
