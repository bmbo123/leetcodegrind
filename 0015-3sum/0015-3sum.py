class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            dic = {}
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                compare = -(nums[i] + nums[j])
                if compare in dic:
                    triplet = [nums[i],nums[j],compare]
                    triplet.sort()
                    triplet = tuple(triplet)
                    res.add(triplet)
                else:
                    dic[nums[j]] = j
        x = []

        for key in res:
            x.append(key)
        return x
                