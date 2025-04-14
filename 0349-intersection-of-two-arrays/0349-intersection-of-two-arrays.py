class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        t= set(nums1)
        s = set(nums2)
        res = []

        for key in s:
            if key in t:
                res.append(key)
        return res
        
        