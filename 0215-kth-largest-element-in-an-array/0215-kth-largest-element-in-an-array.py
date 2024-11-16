class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i] * -1
        heapq.heapify(nums)
        m = 0
        for i in range(k):
            m = heappop(nums)

        return -1 * m

        