class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = 0
        lowest = prices[0]
        for i in range(len(prices)):
            lowest = min(lowest, prices[i])
            curr = max(curr, prices[i]-lowest)
        
        return curr

            