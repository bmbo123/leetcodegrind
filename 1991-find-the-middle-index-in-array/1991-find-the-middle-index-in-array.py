class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pf = []
        sf = [0] * len(nums)
        pf.append(nums[0])

        for i in range(1, len(nums)):
            pf.append(pf[i-1]+nums[i])
        sf[-1] = nums[-1]
        for i in range(len(nums)-2, -1,-1):
            sf[i] = sf[i+1] + nums[i]
        
        for i in range(len(nums)):
            if sf[i] == pf[i]:
                return i
        
        return -1
