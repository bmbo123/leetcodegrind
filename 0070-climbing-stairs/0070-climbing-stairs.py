class Solution:
    def climbStairs(self, n: int,memo = {}) -> int:
        if n in memo:
            return memo[n]
        if n == 1:
            return n
        if n == 2:
            return n
        
        memo[n] = self.climbStairs(n-1,memo) + self.climbStairs(n-2, memo)

        return memo[n]


        
