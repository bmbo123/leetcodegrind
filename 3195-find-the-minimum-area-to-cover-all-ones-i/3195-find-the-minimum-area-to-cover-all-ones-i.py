class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        area = 0
        mx, my = float('inf'), float('inf')
        x, y = 0, 0 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    x = max(i, x)
                    y = max(j, y)
                    mx = min(mx,i)
                    my = min(my, j)
                    print(x,y, mx, my)
                     
        print(x,y, mx, my)
        area = (x-mx+1) * (y-my+1)
        return area 