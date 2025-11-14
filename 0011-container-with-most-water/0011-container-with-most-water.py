class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = 0
        curr = 0
        L, R = 0, len(height)-1

        while R > L:
            x = min(height[R], height[L])
            base = R-L
            curr = max(curr, base * x)

            if height[L] < height[R]:
                L+= 1
            else:
                R-= 1

        return curr

        