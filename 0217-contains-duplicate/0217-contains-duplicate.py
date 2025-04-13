class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = []
        for x in nums:
            if x in res:
                return True
            
            res.append(x)
        return False
        