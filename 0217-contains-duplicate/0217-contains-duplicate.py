class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = set()
        for x in nums:
            if x in res:
                return True
            
            res.add(x)
        return False
        