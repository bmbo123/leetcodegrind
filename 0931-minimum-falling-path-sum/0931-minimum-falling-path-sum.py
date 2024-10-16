class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[float('inf')] * n for _ in range(n)]
        dp[0] = matrix[0]
        for i in range(1,len(matrix)):
            for col in range(len(matrix)):
                if col == n-1:
                    dp[i][col] = matrix[i][col] + min(dp[i-1][col], dp[i-1][col-1])
                elif col == 0:
                    dp[i][col] = matrix[i][col] + min(dp[i-1][col], dp[i-1][col+1])
                else:
                    dp[i][col] = matrix[i][col] + min(dp[i-1][col], dp[i-1][col-1],dp[i-1][col+1])


        return min(dp[-1])
        
