class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        
        front = [0]* len(height)
        back = [0] * len(height)
        back[-1] = height[-1]
        
        for i in range(len(height)):
            front[i] = max(height[i], front[i-1])
        
        for i in range(len(height)-2, -1, -1):
            back[i] = max(height[i], back[i+1])
        
        for i in range(1, len(height)-1):
              
            t = min(front[i-1], back[i+1])
            
            ### the max height on both sides, which gives me the sides of the contianer that hold the value at this specific index 
            t = max(t - height[i], 0)
            water += t
        
        return water
            
            