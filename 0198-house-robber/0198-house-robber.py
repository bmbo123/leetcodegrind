class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 1:
            return nums[0]
        
        dp = [0]*(len(nums)+1)
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2,len(nums)+1):
            dp[i] =max(dp[i-1],nums[i-1]+ dp[i-2])
        

        return dp[-1]



        