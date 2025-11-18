class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        m = float("inf")
        L = 0
        curr = 0

        for i in range(len(nums)):
            curr += nums[i]
            print(curr)
            while curr >= target:
                m = min(m, i-L+1)
                curr -= nums[L]
                L += 1
        

        if m == float("inf"):
            return 0
        else:
            return m
            



