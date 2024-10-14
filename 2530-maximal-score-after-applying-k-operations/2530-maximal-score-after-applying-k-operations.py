class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:

        nums = [-n for n in nums]
        heapq.heapify(nums)
        score = 0
        for i in range(k):
            x =  heapq.heappop(nums)
            score += x
            heapq.heappush(nums, x//3)
        return -score
             