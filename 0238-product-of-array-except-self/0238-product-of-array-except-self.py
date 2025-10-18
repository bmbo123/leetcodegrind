class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = []
        backward = [0] * len(nums)
        forward.append(nums[0])
        backward[-1] = nums[-1]
        for i in range(1,len(nums)):
            forward.append(nums[i]*forward[i-1])
        for i in range(len(nums)-2, -1, -1):
            print(nums[i] * backward[i+1])
            backward[i]= nums[i] * backward[i+1]
        print(forward)
        print(backward)
        res = []

        for i in range(len(nums)):
            if i == 0:
                res.append(backward[i+1])
                continue
            if i == len(nums)-1:
                res.append(forward[i-1])
                continue
            x = forward[i-1] * backward[i+1]
            res.append(x)
        
        return res
        