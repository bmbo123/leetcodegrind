class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = {}
        count = 0

        for i in nums:
            if i in seen:
                count += seen[i]
                seen[i] += 1
            else:
                seen[i] = 1
        
        return count