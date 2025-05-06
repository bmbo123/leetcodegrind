class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in range(len(nums)):
            add = []
            for j in range(len(res)):
                copy = res[j].copy()
                copy.append(nums[i])
                add.append(copy)
            res.extend(add)
        return res
