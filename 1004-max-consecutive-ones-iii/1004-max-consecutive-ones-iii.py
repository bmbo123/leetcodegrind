class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        delete = 0
        count = float('-inf')
        l , r = 0, 0
        while r < len(nums):
            if nums[r] == 0:
                delete += 1
            while delete > k:
                if nums[l] == 0:
                    delete -= 1
                l += 1
            count = max(r-l+1, count)
            r += 1
        return 0 if count == float('-inf') else count

            