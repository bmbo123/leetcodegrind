class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False]*len(nums)
        def solve(q, n):
            if len(q) == n:
                print(q, n)
                res.append(list(q))
                return
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    q.append(nums[i])
                    solve(q,n)
                    q.pop()
                    used[i] = False
        x = []
        solve(x, len(nums))
        return res

