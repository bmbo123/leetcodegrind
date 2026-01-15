class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        m , n = len(grid)-1, len(grid[0])-1
        count = 0

        def dfs(x, y):

            if x < 0 or x > m or y > n or y < 0:
                return
            
            if grid[x][y] == "1":
                grid[x][y] = "0"
            else:
                return
            
            dfs(x+1,y)
            dfs(x,y+1)
            dfs(x-1,y)
            dfs(x, y-1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i,j)
        
        return count


            
            

            
            
            