class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sp = []
        sp = [0] * n
        sp[-1] = nums[-1]
        pd = []
        final = [0] * n

        for i in range(n-2, -1, -1):
            sp[i] = nums[i] * sp[i+1]
        pd.append(nums[0])
        for i in range(1,n):
            pd.append(nums[i] * pd[i-1])
        final[0] = sp[1]
        final[-1] = pd[n-2]
        for i in range(1,n-1):
            final[i] = sp[i+1] * pd[i-1]
        return final