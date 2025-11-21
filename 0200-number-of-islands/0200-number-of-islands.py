class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        
        def bfs(start, end, count):
            queue = collections.deque([(start, end)])
            while queue:
                curr = queue.popleft()
                x, y = curr
                if x not in range(0, len(grid)) or not y in range(0, len(grid[0])):
                    continue
                if grid[x][y] == "1":
                    queue.append((x-1,y))
                    queue.append((x+1,y))
                    queue.append((x,y-1))
                    queue.append((x,y+1))
                grid[x][y] = "0"

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i , j, count)
        return count
        