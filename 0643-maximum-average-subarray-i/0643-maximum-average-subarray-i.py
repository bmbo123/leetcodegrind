class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l , r = 0, k-1
        M = float('-inf')
        oldsum = sum(nums[l:r+1])
        N = oldsum/k
        M = max(N, M)
        r += 1
        while r < len(nums):
            oldsum -= nums[l]
            l += 1
            oldsum += nums[r]
            r += 1
            N = oldsum/k
            M = max(N, M)
        return M
            