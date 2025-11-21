class Solution:
    def canJump(self, nums: List[int]) -> bool:
        x = 0
        for i in range(len(nums)):
            if x >= len(nums):
                print(x,i)
                return True
            if i > x:
                return False
            x = max(nums[i] + i,x)
        return True
         