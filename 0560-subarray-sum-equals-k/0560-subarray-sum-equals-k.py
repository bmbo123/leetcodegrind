class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            prefix = 0
            for j in range(i,len(nums)):
                prefix += nums[j]
                if prefix == k:
                    count += 1

        return count
        
