class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []

        L, R = 0, n

        for i in range(n):
            res.append(nums[L])
            res.append(nums[R])
            L += 1
            R += 1
        
        return res

        