class Solution:
    def maxArea(self, height: List[int]) -> int:
        most = 0
        L , R = 0 , len(height) -1

        while L < R:
            base= min(height[L], height[R])
            width = R-L
            area = base * width
            most = max(most, area)

            if height[L] < height[R]:
                L += 1
            else:
                R-= 1

        
        return most




