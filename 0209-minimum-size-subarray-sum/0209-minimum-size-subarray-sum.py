class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        ps = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            ps[i+1] = ps[i] + nums[i]
        
        if ps[-1] < target:
            return 0
    

        l = 0

        minw = float('inf')
        for r in range(1, len(nums)+1):
            while ps[r] - ps[l] >= target:
                minw = min(r-l, minw)
                l += 1 
        
        return minw




            








