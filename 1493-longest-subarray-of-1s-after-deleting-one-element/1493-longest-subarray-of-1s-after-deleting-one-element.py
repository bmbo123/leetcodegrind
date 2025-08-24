class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = float('-inf')
        l, r = 0, 0
        delete = 0
        while r < len(nums):
            if nums[r] == 0:
                    delete += 1
            while delete >1:
                if nums[l] == 0:
                    delete -= 1
                l += 1
            count = max(r-l, count)
            r += 1
        return 0 if count == float('-inf') else count




