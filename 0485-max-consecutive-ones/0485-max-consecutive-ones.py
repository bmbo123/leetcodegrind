class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = float('-inf')
        curr = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr += 1
            else:
                count = max(curr, count)
                curr = 0
        count = max(curr, count)
        return count

        