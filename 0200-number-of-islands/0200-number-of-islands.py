class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # visted = set()
        # count = 0
        # def explore(x,y):
            
        #     if 1 and not in visted:
        #         visted.add(current)
        #         explore(top)
        #         explore(left)
        #         explore(right)
        #         explore(bottom)
             
        # for each value:
        #     if value not in visited and 1:
        #         count += 1
        #     explore(val):
            
        # return count
        
        visited = set()
        count = 0
        
        def explore(row,column):
            if row < 0 or row > len(grid)-1 or column < 0 or column > len(grid[0])-1: # boundry detection come back and check this later
                return 
  
            if grid[row][column] == "1" and (row,column) not in visited:
                visited.add((row,column)) #gets specific value and adds it to the set
                explore(row,column-1)#top  row stays,column - 1   
                explore(row-1,column)#left row - 1  = left, column stays 
                explore(row+1,column)# row + 1, column stays
                explore(row,column+1)#down row stays,column + 1
            
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if (row,column) not in visited and grid[row][column] == "1":
                    count+=1
                explore(row,column)
               

        
        return count
            
                
            