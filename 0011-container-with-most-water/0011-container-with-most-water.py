class Solution:
    def maxArea(self, height: List[int]) -> int:
        L = 0
        R = len(height)-1
        maxArea = 0
        while L < R:
            h = min(height[L], height[R])
            w = R-L
            area = h*w
            maxArea = max(area, maxArea)
            if height[L] < height[R]:
                L +=1
            else:
                R -= 1
    
        return maxArea