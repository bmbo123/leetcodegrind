class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i] * -1
        heapq.heapify(nums)
        x = 0
        print(nums)
        for i in range(k):
            x = heapq.heappop(nums)
            print(x)
        return x * -1
        