class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        m = []
        m.append(nums[0])
        s = [0] * len(nums)
        s[-1] = nums[-1]
        for i in range(1, len(nums)):
            add = max(nums[i], m[i-1])
            m.append(add)
        for i in range(len(nums)-2, -1, -1):
            s[i] = max(nums[i],s[i+1])
        ms = 0

        for j in range(1, len(nums)-1):
            ms = max(ms,(m[j - 1] - nums[j]) * s[j + 1])
        return ms



        

            