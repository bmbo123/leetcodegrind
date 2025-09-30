class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def solve(nums, choice, n,l):
            res.append(list(choice))
            for i in range(l,n):
                choice.append(nums[i])
                solve(nums,choice,n,i+1)
                choice.pop()
        solve(nums,[],len(nums),0)
        return res

