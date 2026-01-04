class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        arr = []
        for value in set(nums):
            arr.append(value)
        arr.sort()

        print(arr)

        if len(arr) < 3:
            return max(arr)
        else:
            return arr[-3]




