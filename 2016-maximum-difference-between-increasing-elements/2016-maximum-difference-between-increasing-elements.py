class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return -1
        elif len(nums) == 2:

            return nums[1] - nums[0] if nums[1] - nums[0] > 0 else -1
        m = len(nums) // 2
        left = nums[:m]
        right = nums[m:]
        l = self.maximumDifference(left)
        r = self.maximumDifference(right)
        cd = max(right) - min(left)
        return max(l,r,cd) if max(l,r,cd) > 0 else -1