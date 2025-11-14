class Solution:
    def maxArea(self, height: List[int]) -> int:
        ma = 0
        l = 0
        r = len(height) -1
        while l < r:
            curr = min(height[l], height[r])
            w = r - l
            bh = curr * w
            ma = max(bh, ma)
            if height[r] > height[l]:
                l +=1
            else:
                r -= 1
        return ma